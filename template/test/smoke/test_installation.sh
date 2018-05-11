#!/bin/bash

echo ''
echo 'Final test of installation:'

./[project] --help &> /dev/null

if [ $? != 0 ]
then
    echo 'Error: [Project] [version] installation failed.'
    echo ''
    exit 1
fi

echo '[Project] [version] installation succeeded!'
echo ''
