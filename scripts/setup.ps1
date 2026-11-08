# Equivalent de "make setup" sans make (Windows PowerShell)
Set-Location (Join-Path $PSScriptRoot "..")
docker build -t pfa21-audit .
docker run --rm -v "${PWD}:/work" pfa21-audit python scripts/check_env.py
