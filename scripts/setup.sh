#!/bin/bash
set -e

# Must be invoked with the interactive option: `bash -i path/to/this/file`
# -i interactive mode allows us to properly activate environment from within a script
#    since this will source the correct activation script prior to running this file
#    https://stackoverflow.com/questions/55507519/python-activate-conda-env-through-shell-script


# Make the working directory the repo base
SCRIPTDIR=$(dirname $(realpath "$0"))
REPOHOME=$(dirname "${SCRIPTPATH}")
cd $REPOHOME

# Check for mamba/conda to install dev environment
if [ $(command -v mamba) ]; then
    mamba env update -f environment-dev.yml
elif [ $(command -v conda) ]; then
    conda env update -f environment-dev.yml
else
    echo "Please install conda and/or mamba and try again; pip install not supported yet" 1>&2
    exit 1

    # TODO: 
    #   sync requirements-dev.txt with environment-dev.yml using script from pandas
    #   hook into pre-commit to ensure environments are always syncronized.
fi

# This breaks unless script is executed with -i option `bash -i setup.sh`
conda activate dpug-dev

# Install/enable dpug workshop extension
jupyter nbextension install extensions/dpug --sys-prefix
jupyter nbextension enable dpug/main --sys-prefix --section='tree'

# Install pre-commit hooks
pre-commit install
