#!/usr/bin/env sh
# Equivalent de "make setup" sans make (Linux/macOS)
set -e
cd "$(dirname "$0")/.."
docker build -t pfa21-audit .
docker run --rm -v "$PWD":/work pfa21-audit python scripts/check_env.py
