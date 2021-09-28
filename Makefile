##########################################
# Build folder output:
# _build/
#   notebooks/           -> Raw notebooks converted from .md file. No preprocessing done.
#
# 	participant/
#		01_workshops/    -> Preprocessed notebooks, prepped for participant use
#		02_series/       -> Preprocessed notebooks, prepped for participant use
#		- notebooks are run through Exporter.preprocessors to remove content
#			participants/website don't need (e.g. "speaker note" cells)
#		envrionment.yml  -> Abbreviated version of environment-dev.yml
# 
#   site/
#		- contains preprocessed & executed .rst versions of notebooks ready for sphinx-build
#
#		- all other files rsync'd in from {repo_home}/unconverted
#			  (taking care to not sync the aforementioned notebooks)
#
#   _site/			     -> output of sphinx-build on site/
#		- finalized output to push to gh-pages branch
#
##########################################

SOURCE_DIR     = unconverted
SERIES_DIR     = 01_series
WORKSHOP_DIR   = 02_workshops

# FIND_ARGS      = -name "index.md" -type f -prune -o -name "*.md" -print
# SOURCE_MD = $(shell find "$(SOURCE_DIR)/$(SERIES_DIR)" "$(SOURCE_DIR)/$(WORKSHOP_DIR)" $(FIND_ARGS))
# Only run markdown notebook files through jupyter nbconvert to speed up build
SOURCE_MD = $(shell python scripts/find_markdown_notebooks.py $(SOURCE_DIR))
RSYNC_EXCLUDE_SOURCES = $(addprefix --exclude ,$(subst $(SOURCE_DIR)/,,$(SOURCE_MD)))

BUILD_DIR         = _build
NOTEBOOKS_DIR     = $(BUILD_DIR)/notebooks
BUILT_PARTICIPANT = $(BUILD_DIR)/participant
PREPROC_SITE      = $(BUILD_DIR)/site
BUILT_SITE        = $(BUILD_DIR)/_site

rename_source = $(SOURCE_MD:$(SOURCE_DIR)/%.md=$(1)/%.$(2))

RAW_NOTEBOOKS         = $(call rename_source,$(NOTEBOOKS_DIR),ipynb)
PARTICIPANT_NOTEBOOKS = $(call rename_source,$(BUILT_PARTICIPANT),ipynb)
SITE_NOTEBOOKS        = $(call rename_source,$(PREPROC_SITE),rst)

.PHONY: help all toc html serve clean clean-html

help:
	@echo $(SPHINXOPTS)
	@echo ''
	@echo 'usage: make [target]'
	@echo ''
	@echo 'target'
	@echo '  all:           builds both participant & runs sphinx-build'
	@echo '  participant:   builds ipynb files for participants'
	@echo '  html:          runs sphinx-build on $(PREPROC_SITE) to generate files for $(BUILT_SITE)'
	@echo '  serve:         runs a local server pointed at $(BUILT_SITE) for testing'
	@echo '  clean:         removes $(BUILD_DIR) completely'
	@echo '  clean-html:    removes output of sphinx-build $(BUILT_SITE)'


# target to build everything
all: participant html

notebooks: $(RAW_NOTEBOOKS)

# target for building participant branch
participant: $(PARTICIPANT_NOTEBOOKS)
	@mkdir -p "$(BUILT_PARTICIPANT)"
	@echo "creating participant environment.yml"
	@python scripts/generate_env_from_dev.py --output $(BUILT_PARTICIPANT)

html: $(SITE_NOTEBOOKS)
	@echo "syncing $(SOURCE_DIR)/ to $(PREPROC_SITE)/"
	@rsync -ra --exclude .ipynb_checkpoints $(RSYNC_EXCLUDE_SOURCES) "$(SOURCE_DIR)/" "$(PREPROC_SITE)"

	@sphinx-build -Wnv "$(PREPROC_SITE)" "$(BUILT_SITE)"

# use `tail` to log file name + file contents in {BUILT_SITE}/reports/ (if that folder exists)
	@[ -d "$(BUILT_SITE)/reports" ] && tail -v -n +1 "$(BUILT_SITE)"/reports/*.log || echo ""
	
serve:
	python scripts/serve.py --static-path="$(BUILT_SITE)"

clean:
	@rm -rf $(BUILD_DIR)

clean-html:
	@rm -rf $(BUILT_SITE)


$(RAW_NOTEBOOKS): $(NOTEBOOKS_DIR)/%.ipynb: $(SOURCE_DIR)/%.md
	@mkdir -p $(dir $@)
	@echo "[jupytext] $< -> $*.ipynb"
	@jupytext $< --to notebook --quiet --output $@

# {SRC_DIR}/**.md -> {BUILT_WORKSHOP_DIR}/**.ipynb
$(PARTICIPANT_NOTEBOOKS): $(BUILT_PARTICIPANT)/%.ipynb: $(NOTEBOOKS_DIR)/%.ipynb
	@mkdir -p $(dir $@)
	@echo "[nbconvert] (participant) Preprocessing $*.ipynb"
	@jupyter nbconvert $< \
		--to notebook \
		--output-dir $(dir $@) \
		--Exporter.preprocessors nbpreprocess.RemoveSlideShowNotesCells

# {BUILT_NOTEBOOK_DIR}/**.ipynb -> {BUILT_HTML_DIR}/**.html
$(SITE_NOTEBOOKS): $(PREPROC_SITE)/%.rst: $(NOTEBOOKS_DIR)/%.ipynb
	@mkdir -p $(dir $@)
	@echo "[nbconvert] (website) Preprocessing $*.rst"
	@jupyter nbconvert $< \
		--to nbpreprocess.NbSphinxRST \
		--output-dir $(dir $@) \
		--execute
