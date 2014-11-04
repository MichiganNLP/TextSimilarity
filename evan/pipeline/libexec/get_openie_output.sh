#!/usr/bin/env bash
set -e

DIRNAME="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$DIRNAME/config.sh"

cd "$OPENIE_DIRECTORY"
sbt "run-main edu.knowitall.openie.OpenIECli --format column $input $output"
cd - > /dev/null
