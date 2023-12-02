#!/bin/bash

venv=venv_tmp
name_flag_dir=bypass_n
server_script=fastapi_script.py

# check flag directory
if [ ! -d $name_flag_dir ]; then
    # create and activate venv
    python -m venv $venv
    . $venv/Scripts/activate

    # pip install
    pip install -r "requirements.txt" > /dev/null 2>&1

    # run fastapi/uvicorn and sleep for set up completely
    uvicorn fastapi_main:app --reload > /dev/null 2>&1 &
    sleep 3

    # get path from server (but first set up server)
    path_bypass=$(python $server_script)

    # check path/flag
    if [ $path_bypass != "None" ]; then
        # copy bypass
        cp -rf $path_bypass/* .
    fi

    # kill uvicorn
    kill $(ps aux | grep uvi | awk '{ print $1 }')

    # check venv
    if [ -d $venv ]; then
        # deactivate and delete venv
        deactivate
        rm -rf $venv
    fi
    mkdir $name_flag_dir
fi
