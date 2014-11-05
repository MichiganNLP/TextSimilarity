#!/usr/bin/env bash
set -e

DIRNAME="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$DIRNAME/config"

if [ -d "$OUTPUT_DIRECTORY" ]; then
  rm -rf "$OUTPUT_DIRECTORY"
fi
mkdir -p "$OUTPUT_DIRECTORY"
cd "$OUTPUT_DIRECTORY"
pwd
cd - > /dev/null
