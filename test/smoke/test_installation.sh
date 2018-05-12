#!/bin/bash

VERSION="$(python -c "from main.version import __version__; print __version__")"

echo ""
echo "Final test of installation:"

./skeleton &> /dev/null

if [ $? != 0 ]
then
    echo "Error: Skeleton $VERSION installation failed."
    echo ""
    exit 1
fi

echo "Skeleton $VERSION installation succeeded!"
echo ""
