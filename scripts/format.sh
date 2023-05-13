#!/bin/bash -e

PACKAGE_PATH="devblaze"

ruff "$PACKAGE_PATH" --fix
black "$PACKAGE_PATH"