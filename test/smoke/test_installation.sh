#!/bin/bash

echo ''
echo 'Final test of installation:'

./skeleton &> /dev/null

if [ $? != 0 ]
then
    echo 'Error: Skeleton 0.1.0 installation failed.'
    echo ''
    exit 1
fi

echo 'Skeleton 0.1.0 installation succeeded!'
echo ''
