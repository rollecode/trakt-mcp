#!/usr/bin/env bash
#
# Regenerate openapi.json from Trakt's own contract package.
#
# Trakt publishes no OpenAPI file, but trakt/api-help carries typed contracts
# for every endpoint and a task that turns them into one. Running their
# generator beats parsing the contracts ourselves: it is the same document
# Trakt's own tooling consumes.
#
#   scripts/fetch_spec.sh

set -euo pipefail

CHECKOUT=${CHECKOUT:-$(mktemp -d)}
OUT=${OUT:-openapi.json}

command -v deno >/dev/null || { echo "deno is required" >&2; exit 1; }

git clone -q --depth 1 https://github.com/trakt/api-help.git "$CHECKOUT"
( cd "$CHECKOUT" && deno install --allow-scripts --frozen >/dev/null )
( cd "$CHECKOUT/projects/openapi" && deno task generate >/dev/null )

# The full document is over 5 MB of response schemas. The generator only reads
# paths, methods, summaries and parameters, so the rest is dropped.
python3 - "$CHECKOUT/projects/openapi/openapi.json" "$OUT" <<'PY'
import json
import sys

full = json.load(open(sys.argv[1]))
slim = {"openapi": full.get("openapi", "3.0.3"), "info": full.get("info", {}), "paths": {}}

for path, methods in full["paths"].items():
    for method, operation in methods.items():
        parameters = []
        for parameter in operation.get("parameters") or []:
            kept = {k: v for k, v in parameter.items()
                    if k in ("name", "in", "required", "description", "schema")}
            schema = kept.get("schema") or {}
            kept["schema"] = {"type": schema.get("type", "string")}
            parameters.append(kept)

        entry = {
            "summary": operation.get("summary") or "",
            "tags": operation.get("tags") or [],
            "parameters": parameters,
        }
        if operation.get("requestBody"):
            entry["requestBody"] = {
                "required": operation["requestBody"].get("required", False),
                "content": {"application/json": {"schema": {"type": "object"}}},
            }
        slim["paths"].setdefault(path, {})[method] = entry

json.dump(slim, open(sys.argv[2], "w"), indent=1)
operations = sum(len(m) for m in slim["paths"].values())
print(f"{len(slim['paths'])} paths, {operations} operations -> {sys.argv[2]}")
PY
