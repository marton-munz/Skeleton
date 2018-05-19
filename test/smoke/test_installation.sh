#!/bin/bash

echo ""
echo "---------------------------------------------------------------------------------------"

VERSION="$(python -c "from main.version import __version__; print __version__")"

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

echo "Smoke test of installation:"

./skeleton &> /dev/null

if [ $? != 0 ]
then
    echo "${red}Error: Skeleton $VERSION installation failed.${reset}"
    echo "---------------------------------------------------------------------------------------"
    echo ""
    exit 1
fi


echo "${green}Skeleton $VERSION installation succeeded!${reset}"
echo "---------------------------------------------------------------------------------------"
echo ""