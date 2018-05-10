#!/bin/bash

echo ''
echo 'Checking [Project] installation'

./[project] --help &> /dev/null

if [ $? != 0 ]
then
    echo 'Error: [Project] installation failed.'
    exit 1
fi

echo '[Project] installation succeeded'
echo ''
