#!/bin/bash
set -e

case "$1" in
    "run")
        exec python -m ...
    ;;
    *)
        exec ${@}
    ;;
esac