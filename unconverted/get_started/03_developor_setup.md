# Developer setup

It is highly recommended that you invoke the the `setup.sh` script to set up your developer environment. There are numerous pieces in this project that need to be properly managed/installed

From your terminal run:
```bash
bash -i scripts/setup.sh
```
*Why specify the `-i` option in the above snippet?*
- the `setup.sh` file create an anaconda environment and then activates to install the remaining dependencies. In order to activate the environment from within a script, we need to invoke the script in "interactive"
