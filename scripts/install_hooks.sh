#!/bin/bash
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit
echo "Git hooks installed and configured!"
