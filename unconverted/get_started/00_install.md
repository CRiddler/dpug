# Installation Guide

Welcome to this set up guide

## What are we installing?
**bash**: `bash` comes with Mac and Linux but is not natively installed on Windows. `Bash` is a powerful command line interface that allows you to efficiently manipulate files and directories. You will also use it to access and interact with `git` (version control).

**git**: `git` is a tool that you use to keep track of changes in your documents. This makes your workflow more reproducible. It also allows you to undo changes that you want to undo!

**conda**: `conda` is a package and environment management tool that allows you to install Python packages on your computer as well as create and manage multiple Python environments, each containing different packages. To get started with conda and Python, you will install the Miniconda Python distribution, which provides both the conda package manager and a basic Python environment. You will then install the `dpug` conda environment which will provide all of the specific libraries/packages you will need.

## Install Bash
````{tabbed} Windows
Install WSL

````
````{tabbed} Mac
The default shell in all versions of Mac OS X is Bash, so no need to install anything. You access Bash from the Terminal (found in /Applications/Utilities). You may want to keep Terminal in your dock for this workshop.
````
````{tabbed} Linux
The default shell is usually Bash but if your machine is set up differently you can run it by opening the Terminal and typing: bash. There is no need to install anything.
````

## Install Git
````{tabbed} Windows
1. Open the WSL Terminal
2. Run the following command:
    ```
    sudo apt-get install git
    ```
````
````{tabbed} Mac
Git on Mac OS X

[Video Tutorial](https://www.youtube.com/watch?v=9LQhwETCdwY)

Install Git on Macs by downloading and running the most recent installer for “mavericks” if you are using OS X 10.9 and higher -or- if using an earlier OS X, choose the most recent “snow leopard” installer, from [this list](https://sourceforge.net/projects/git-osx-installer/files/).

After installing Git, there will not be anything in your /Applications folder, as Git is a command line program.

**Note: If you are running Mac OSX El Capitan, you might encounter errors when trying to use Git. Make sure you update XCODE. [Read more - a Stack Overflow Issue](https://stackoverflow.com/questions/32893412/command-line-tools-not-working-os-x-el-capitan-sierra-high-sierra-mojave).**
````
````{tabbed} Linux
If Git is not already available on your machine, you can try to install it via your distro’s package manager. For Debian/Ubuntu, run `sudo apt-get install git` and for Fedora run `sudo yum install git`.
````

## Install Miniconda
````{tabbed} Windows
**IMPORTANT**: if you already have a Python installation on your Windows computer, the settings below will replace it with Miniconda Python 3.x as the default Python. If you have questions or concerns about this, please contact your course instructor.

Download the [Miniconda installer for Windows](https://docs.conda.io/en/latest/miniconda.html#windows-installers). Be sure to download the Python 3.x version!

Run the installer by double-clicking on the downloaded file and follow the steps below.

1. Click “Run”.
2. Click on “Next”.
3. Click on “I agree”.
4. Leave the selection on “Just me” and click on “Next”.
5. Click on “Next”.
6. **Select the first option for “Add Anaconda to my PATH environment variable” and also leave the selection on “Register Anaconda as my default Python 3.9”. Click on “Install”.**
    Note that even though the installation is for Miniconda, the installer uses the word Anaconda in these options. You will also see a message in red text that selecting “Add Anaconda to my PATH environment variable” is not recommended; continue with this selection to make using conda easier in Git Bash. If you have questions or concerns, please contact your instructor.
7. When the install is complete, Click on “Next”.
8. Click on “Finish”.
````
````{tabbed} Mac
1. Download the installer: [Miniconda installer for Mac](https://docs.conda.io/en/latest/miniconda.html). Be sure to download the Python 3.x version!

2. In your Terminal window, run:
    ```bash
    bash Miniconda3-latest-MacOSX-x86_64.sh
    ```

3. Follow the prompts on the installer screens.

4. If you are unsure about any setting, accept the defaults. You can change them later.

5. To make sure that the changes take effect, close and then re-open your Terminal window.
````
````{tabbed} Linux
1. Download the installer: Miniconda installer for Linux. Be sure to download the Python 3.x version!
2. In your Terminal window, run: bash Miniconda3-latest-Linux-x86_64.sh.
3. Follow the prompts on the installer screens.
4. If you are unsure about any setting, accept the defaults. You can change them later.
5. To make sure that the changes take effect, close and then re-open your Terminal window.
````

## Test your set-up of Bash, Git and Miniconda
````{tabbed} Windows
1. Search for and open the WSL program. In this Terminal window, type bash and hit enter. If you do not get a message back, then Bash is available for use.

2. Next, type git and hit enter. If you see a list of commands that you can execute, then Git has been installed correctly.

3. Next, type conda and hit enter. Again, if you see a list of commands that you can execute, then Miniconda Python has been installed correctly.

4. Close the Terminal by typing exit.
````
````{tabbed} Mac
Search for and open the Terminal program (found in /Applications/Utilities). In this Terminal window, type bash and hit enter. If you do not get a message back, then Bash is available for use.

Next, type git and hit enter. If you see a list of commands that you can execute, then Git has been installed correctly.

Next, type conda and hit enter. Again, if you see a list of commands that you can execute, then Miniconda Python has been installed correctly.

Close the Terminal by typing exit.
````
````{tabbed} Linux
Search for and open the Terminal program. In this Terminal window, type bash and hit enter. If you do not get a message back, then Bash is available for use.

Next, type git and hit enter. If you see a list of commands that you can execute, then Git has been installed correctly.

Next, type conda and hit enter. Again, if you see a list of commands that you can execute, then Miniconda Python has been installed correctly.

Close the Terminal by typing exit.
````

```{note}
Adapted from [earthdatascience](https://www.earthdatascience.org/workshops/setup-earth-analytics-python/).
Copyright (c) Earth Lab
```
