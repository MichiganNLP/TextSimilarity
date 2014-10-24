#!/usr/bin/env bash
set -e

DIRNAME="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$DIRNAME/config.sh"

cd "$OPENIE_DIRECTORY"

sbt 'run-main edu.knowitall.openie.OpenIECli' < "$input_file" > /tmp/openie_output
cat /tmp/openie_output | sed -r "s/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g"  # removes coloring

cd - > /dev/null
