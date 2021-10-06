# Developer Set up:
## Pre-Reqs
* `git`
* `conda` or `mamba`
* A bash shell

## Steps
* `git clone` the repo
* `bash -i scripts/setup.sh`
  * installs "dpug-dev" environment from envrionment-dev.yml
  * installs dpug jupyter notebook extension (NOT a jupyter lab extension)
  * installs pre-commit hooks
* Makefile commands (also see `make help`)
  * `all`:           builds both participant & html files for web
  * `participant`:   builds ipynb files for participants
  * `html`:          runs sphinx-build on _build/site to generate files for _build/_site/index.html
  * `serve`:         runs a local server pointed at `_build/_site` for testing
  * `clean`:         removes _build completely
  * `clean-html`:    removes output of sphinx-build `_build/_site`


# TODO:
- implement watchdog/inotify for makefile when using `make serve`
  - utilize jupyter-cache to allow for faster remakes of changed markdown notebooks?
- implement "dpug" -> "status": ["draft", "publish"] notebook metadata
  - "draft": notebooks are built via the makefile, however they are removed from final
      output, to prevent them from being pushed to the participant & gh-pages branches
  - "publish": same as draft, but notebooks are not removed prior to deployment.
- Fix admonition support, may need to refactor build process for this
- requirements-dev.txt for developers who use some other env manager? Can synchronize with pandas `scripts/gen_pip_from_conda.py` pre-commit hook
- Move all of the text below this todo list to appropriate locations

## Workshop Conceptual Format:
- Topics should aim to bridge the gap between beginner and intermediate programmer
- Try to answer the questions:
  - "I know the basics, now what?"
  - "Something that I was never explicitly taught, but use every day is..."
- 30 minute total, designed for 15 minutes of content (time at end is okay, over time is bad)
- End with a challenge! Learning by doing is the best way to code

## Creating a New Workshop:
- Ensure you have an environment set up with the requirements from `./environment-dev.yml`  
Also read through: [notebooks as .md files](https://jupytext.readthedocs.io/en/latest/formats.html#markdown-formats)

- Start a jupyter notebook session at the workshops folder
- Create a new .ipynb file under the `./notebooks/` folder
  - Upon saving, a corresponding `.md` file will be appear under the `./markdown/` folder. This is the file that will be pushed to github to provide meaningful diffs.
- Create markdown/code cells as you would in a notebook.
- To link static files, store static files in the `/static/` folder and reference them within your notebook.  
(should we embed static files within the notebook? Makes for easier downloading by the user?)

## Editing a Workshop
- Once jupytext is installed you should be able to edit the .md files as if they were jupyter notebooks
- TODO: implement `jupytext --sync` as a pre-commit hook which will allow us to operate on the notebooks and synchronize back to the .md format prior to a commit. 

## Jupytext/Jupyter Extra Notes:
### Configure a notebook to allow errors
- Since we will convert all .md files to .ipynb, we will need to programmatically run
each notebook
- "View -> Cell Toolbar -> Tags"
- in the cell you wish to allow an error in, add the tag "raises-exception"

## Configure a notebook as a slideshow
- To configure the .md files as a presentation, click "View -> Cell Toolbar -> Slideshow". Then configure each cell to be part of the slideshow itself. See [presenting with jupyter](https://medium.com/@Ben_Obe/introduction-to-presenting-with-juypter-with-reveal-js-8e34a07081b2)
