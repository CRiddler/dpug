# Contributing
Thank you for your interest in contributing to dpug. Whether you are a UC Davis data 
lab member/affialiate, a curious student, or another interested party, you'll find out 
how to contribute to our growing repository of talks, workshops, and other resources 
below.

This guide starts with a general description of the different ways to contribute
to the dpug repository, then we explain some technical aspects of preparing your
contribution. We discuss in detail the appropriate `git` commands to run as we 
are aware many of our contributors are new to `git`. If anything in this guide is unclear,
please do not hesitate to contact: **{some contact info here?}** as we would like this guide
to be as concise and understandable as possible.

## Have a Bug Report?
Some piece of code not working? Submit a bug report [here](https://github.com/CRiddler/dpug/issues).


# Setting up your workspace
Please see README_setup.md



## Making a development branch
Don't work in the main branch. As soon as you get your main branch ready, run:

DO THIS (but change the branch name)
```bash
git checkout -b my-dev-branch
```

## Pull Request When Ready
If you've made changes to a markdown notebook, ensure that it runs without error-
* restart kernel & run all

Push the changes to your forked repository, and submit a pull request back to the origin
branch from the branch you've worked in.
