#!/usr/bin/env bash
set -e

DIRNAME="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$DIRNAME/config"

cd "$output"

virtualenv env
source env/bin/activate

pip install beautifulsoup4

cd - > /dev/null
