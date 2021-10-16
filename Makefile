##########################################
# Build folder output:
# _build/
# 	participant/
#		workshops/       -> Preprocessed notebooks, prepped for participant use
#		series/          -> Preprocessed notebooks, prepped for participant use
#		- notebooks are run through Exporter.preprocessors to remove content
#			participants/website don't need (e.g. "speaker note" cells)
#		envrionment.yml  -> Abbreviated version of environment-dev.yml
#								see scripts/generate_env_from_dev.py
#
#   html/			     -> output of sphinx-build on site/
#		- finalized output to push to gh-pages branch
#
##########################################

SPHINX_OPTS = -WT -b html
SOURCE_DIR     = unconverted
BUILD_DIR      = _build

BUILT_HTML        = $(BUILD_DIR)/html
BUILT_PARTICIPANT = $(BUILD_DIR)/participant

MD_NOTEBOOKS = $(shell python scripts/find_markdown_notebooks.py $(SOURCE_DIR))
PARTICIPANT_NOTEBOOKS = $(MD_NOTEBOOKS:$(SOURCE_DIR)/%.md=$(BUILT_PARTICIPANT)/%.ipynb)


.PHONY: help html participant clean clean-html clean-participant clean-cache serve

help:
	@echo 'Usage: make [target]'
	@echo '  targets:'
	@echo '    html               Builds html files for website'
	@echo '    participant        Builds notebooks for participant & binder use'
	@echo '    all                Builds both html & notebooks'
	@echo '    clean              Removes $(BUILD_DIR) folder entirely'
	@echo '    clean-html         Removes $(BUILT_HTML) folder'
	@echo '    clean-participant  Removes $(BUILT_PARTICIPANT) folder'
	@echo '    clean-cache        Removes $(BUILD_DIR)/{.jupyter_cache,jupyter_execute}'
	@echo '                         These folders are automatically created when building'
	@echo '                         site html and are used to speed up notebook executions'
	@echo '    serve              Runs a simple local server that serves $(BUILT_HTML)'
	@echo '                         while also watching $(SOURCE_DIR) to rebuild the site'
	@echo '                         when a change in $(SOURCE_DIR) occurs'

html:
	@sphinx-build $(SPHINX_OPTS) "$(SOURCE_DIR)" "$(BUILT_HTML)"

participant: $(PARTICIPANT_NOTEBOOKS)
	@mkdir -p "$(BUILD_DIR)/participant"
	@echo "creating environment.yml"
	@python scripts/generate_env_from_dev.py --output "$(BUILD_DIR)/participant"

all: html participant

clean:
	@rm -rf "$(BUILD_DIR)"

clean-html:
	@rm -rf "$(BUILT_HTML)"

clean-participant:
	@rm -rf "$(BUILT_PARTICIPANT)"

clean-cache:
	@rm -rf "$(BUILD_DIR)/.jupyter_cache" "$(BUILD_DIR)/jupyter_execute"

serve:
	@sphinx-autobuild $(SPHINX_OPTS) "$(SOURCE_DIR)" "$(BUILD_DIR)/html"


$(PARTICIPANT_NOTEBOOKS): $(BUILT_PARTICIPANT)/%.ipynb: $(SOURCE_DIR)/%.md
	@mkdir -p $(dir $@)
	@jupytext "$<" \
		--to notebook \
		--output "$@"

	@jupyter nbconvert $@ \
		--to notebook \
		--inplace     \
		--Exporter.preprocessors nbpreprocess.RemoveSlideShowNotesCells
