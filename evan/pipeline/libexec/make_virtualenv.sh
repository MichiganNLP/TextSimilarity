#!/usr/bin/env bash
set -e

DIRNAME="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$DIRNAME/config.sh"

cd "$output"

virtualenv env
source env/bin/activate
pip install -r "$DIRNAME/../res/python-requirements.txt"

cd - > /dev/null
