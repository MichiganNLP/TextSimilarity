#!/usr/bin/env bash
set -e

DIRNAME="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$DIRNAME/config.sh"

cd "$output/permutations"
cat *.txt > /tmp/combined-permutations
cd - > /dev/null

cd "$SEMAFOR_RELEASE_DIRECTORY"
mkdir -p temp
./fnParserDriver.sh /tmp/combined-permutations "$output/semafor_output.xml"
rm -rf temp
cd - > /dev/null
