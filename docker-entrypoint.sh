#!/bin/bash
set -e

case "$1" in
    "run")
        exec python -m src.main
    ;;
    *)
        exec ${@}
    ;;
esac