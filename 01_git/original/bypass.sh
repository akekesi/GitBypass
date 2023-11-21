#!/bin/bash

name_copy_dir=original                  # name of the folder to copy
name_cloned_git=bypass_git              # name of rhe cloned git repository
path_bypass_y=$name_cloned_git/bypass_y # relative path of bypass folder with flag y: yes, use bypass
path_bypass_n=$name_cloned_git/bypass_n # relative path of bypass folder with flag n: no, do not use bypass
git_ssh=git@github.com:akekesi/GitBypass-Git.git

if [ ! -d $name_cloned_git ]; then
    git clone $git_ssh $name_cloned_git > /dev/null 2>&1
fi

if [ -d $path_bypass_y ]; then
    cp -rf $path_bypass_y/$name_copy_dir/* .
    mv $path_bypass_y $path_bypass_n
fi
