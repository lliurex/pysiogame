#!/bin/sh --

OLD_DIR="`pwd`"
cd "/usr/share/games/pysiogame/"
python3 /usr/share/games/pysiogame/eduactiv8.py "$@"
cd "$OLD_DIR"
