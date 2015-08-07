#!/bin/bash
# Walker 2015.08.07

PROFILE='profile_default'


if [ -d ~/.ipython/$PROFILE/ ]; then
    echo "Copy config.py file"
    cp ipython_notebook_config.py ~/.ipython/$PROFILE/
fi

if [ -d ~/.ipython/$PROFILE/static/custom/ ]; then
    echo "Copy custom.js file"
    cp custom.js ~/.ipython/$PROFILE/static/custom/
fi 

ls -al ~/.ipython/$PROFILE/ipython_notebook_config.py
ls -al ~/.ipython/$PROFILE/static/custom/custom.js

echo "run with 'ipython notebook'"

