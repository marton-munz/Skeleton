#!/bin/bash

VERSION="$(python -c "from main.version import __version__; print __version__")"

echo ""
echo "Final test of installation:"

./[project] --help &> /dev/null

if [ $? != 0 ]
then
    echo "Error: [Project] $VERSION installation failed."
    echo ""
    exit 1
fi

echo "[Project] $VERSION installation succeeded!"
echo ""
