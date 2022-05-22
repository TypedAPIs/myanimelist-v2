# This file should be changed for every project.

BASEDIR="$(dirname "$(dirname "$0")")"

# JS support

JS_DATA_DIR="$BASEDIR/js/tests/data"

mkdir -p "$JS_DATA_DIR"

# Python support

function jsonToPython() {
    # Usage: jsonToPython <json file> <python file>
    python3 -c $'import json, sys\nprint("data = " + repr(json.loads(sys.stdin.read())))' < "$1" > "$2"
}

PY_DATA_DIR="$BASEDIR/python/tests/examples"

mkdir -p "$PY_DATA_DIR"
