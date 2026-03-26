#!/bin/bash

# Disable path conversion for Windows Git Bash
export MSYS_NO_PATHCONV=1

echo "Create a template dir to allow Hugo properly clone the modules"
mkdir -p themes/docsy

echo "Open local browser on port 1313"
docker run \
    -v $PWD:/src \
    --rm \
    --user root \
    --name sw360_website \
    -p 1313:1313 \
    "$@" \
    hugomods/hugo:exts-non-root \
    server --logLevel debug --cleanDestinationDir \
    --baseURL http://localhost:1313/sw360
