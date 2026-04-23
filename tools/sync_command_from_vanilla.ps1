# Sync ERB/○TRAIN/COMMAND from vanilla install; keep modded COM200-299_道具.ERB
# Usage: .\sync_command_from_vanilla.ps1  [path-to-vanilla\ERB\○TRAIN\COMMAND]
param([string]$VanillaCommandDir = "")

$ErrorActionPreference = "Stop"
if ($VanillaCommandDir -eq "") {
    $VanillaCommandDir = "C:\Users\范振宁\Downloads\era\ERB\○TRAIN\COMMAND"
}
$src = $VanillaCommandDir
$dst = Join-Path (Split-Path $PSScriptRoot -Parent) "ERB\○TRAIN\COMMAND"
$keep = "COM200-299_道具.ERB"

if (-not (Test-Path -LiteralPath $src)) {
    Write-Error "Source not found: $src`nPass the folder as first argument, or edit default in this script."
    exit 1
}
if (-not (Test-Path -LiteralPath $dst)) {
    New-Item -ItemType Directory -Path $dst -Force | Out-Null
}

Get-ChildItem -LiteralPath $src -File | ForEach-Object {
    if ($_.Name -eq $keep) { return }
    Copy-Item -LiteralPath $_.FullName -Destination (Join-Path $dst $_.Name) -Force
    Write-Host "OK $($_.Name)"
}
Write-Host "Done. ($keep in dest was not overwritten from vanilla.)"
