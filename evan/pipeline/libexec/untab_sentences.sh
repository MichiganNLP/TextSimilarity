#!/usr/bin/env bash
set -e

cat "$filename" | sed "s|\t|\n|"
