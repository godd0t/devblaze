#!/bin/bash -e

PACKAGE_PATH="devblaze"

ruff "$PACKAGE_PATH"
black "$PACKAGE_PATH" --check
