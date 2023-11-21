#!/bin/bash

if [ "$#" -eq 0 ]; then
    echo "No argument/No folder to copy"
else
    path_orig=$1
    path_test="99_test"

    cp -rf "$path_orig" "$path_test"
fi