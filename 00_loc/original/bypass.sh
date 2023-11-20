#!/bin/bash

path_bypass_y=../bypass_y   # relative path of bypass folder with flag y: yes, use bypass
path_bypass_n=../bypass_n   # relative path of bypass folder with flag n: no, do not use bypass
name_copy_dir=original      # name of the folder to copy

if [ -d $path_bypass_y ]; then
    cp -rf $path_bypass_y/$name_copy_dir/* .
    mv $path_bypass_y $path_bypass_n
fi
