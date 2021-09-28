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

    # pip setup details (untested)
    # TODO: ensure some type of virtual env is used?
    
    # reconfigure scripts/generate_pip_deps_from_conda.py from Pandas github as a pre-commit
    # This will ensure that environment.yml is synced with requirements.txt on commit
    # pip install -r requirements-dev.txt

    # install jupyter extensions (conda does this automatically)
    # jupyter contrib nbextension install all --sys-prefix

    # TODO: install ruby-devkit (or install ruby + compilers?)
fi

# This breaks unless script is executed with -i option `bash -i setup.sh`
conda activate dpug-dev

# Install/enable dpug workshop extension
jupyter nbextension install extensions/dpug --sys-prefix
jupyter nbextension enable dpug/main --sys-prefix --section='tree'

# Install pre-commit hooks
pre-commit install
