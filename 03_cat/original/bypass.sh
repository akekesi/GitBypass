#!/bin/bash

venv=venv_tmp
configcat_script=configcat.py
name_copy_dir=original                  # name of the folder to copy
name_cloned_git=bypass_git              # name of rhe cloned git repository
path_bypass_y=$name_cloned_git/bypass_y # relative path of bypass folder with flag y: yes, use bypass
path_bypass_n=$name_cloned_git/bypass_n # relative path of bypass folder with flag n: no, do not use bypass
git_ssh=git@github.com:akekesi/GitBypass-Git.git

# check git repository
if [ ! -d $name_cloned_git ]; then
    # create and activate venv
    python -m venv $venv
    . $venv/Scripts/activate

    # pip install
    pip install -r "requirements.txt" > /dev/null 2>&1

    # call configcat script
    configcat_output=$(python $configcat_script)

    # check configcat
    if [ $configcat_output = "True" ] && [ ! -d $name_cloned_git ]; then
        # clone git
        git clone $git_ssh $name_cloned_git > /dev/null 2>&1
    fi
fi

# check flag
if [ -d $path_bypass_y ]; then
    # copy bypass
    cp -rf $path_bypass_y/$name_copy_dir/* .
    mv $path_bypass_y $path_bypass_n
fi

# check venv
if [ -d $venv ]; then
    # deactivate and delete venv
    deactivate
    rm -rf $venv
fi
