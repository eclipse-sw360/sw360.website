#!/bin/bash

echo "Create a template dir to allow Hugo properly clone the modules"
mkdir -p themes/docsy

echo "Open local browser on port 1313"
docker run -v $PWD:/src --rm --name sw360_website -p 1313:1313 $@ klakegg/hugo:0.93.2-ext-ubuntu server --verbose --verboseLog --debug --cleanDestinationDir --baseUrl http://localhost:1313/sw360
