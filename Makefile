.PHONY: clean all

# Find all of the notebooks by searching the `notebooks` directory of icepack
# for anything that ends with `.ipynb` and isn't a directory and sort them
NOTEBOOK_FILES:=$(shell find ${ICEPACK}/notebooks -not -path '*/\.*' -type f -name '*\.ipynb' | sort)

# Make a target containing all of the imported, executed demos; to get any
# executed demo from its source in icepack, call `jupyter nbconvert`.
executed-notebooks: $(patsubst ${ICEPACK}/notebooks/%.ipynb,executed-notebooks/%.ipynb,$(NOTEBOOK_FILES))
executed-notebooks/%.ipynb: ${ICEPACK}/notebooks/%.ipynb
	jupyter nbconvert \
	    --to ipynb \
	    --execute \
	    --ExecutePreprocessor.timeout=24000 \
	    --output-dir=`dirname $@` \
	    --output=`basename $@` \
	    $<

# To get any demo page from an executed demo, call `nikola new_page`, extract
# the title of the demo from its raw source, and import it. Next, use jq and
# sponge to add an attribute to the notebook metadata that tells nikola to hide
# the page title. The title is part of the notebook anyway.
notebooks: $(patsubst ${ICEPACK}/notebooks/%.ipynb,pages/notebooks/%.ipynb,$(NOTEBOOK_FILES))
pages/notebooks/%.ipynb: executed-notebooks/%.ipynb
	rm -f $@
	nikola new_page \
	    --format ipynb \
	    --title="$$(python3 extract_title.py $<)" \
	    --import=$< \
	    $@
	jq '.metadata.nikola += {hidetitle: "True"}' $@ | sponge $@

# Make the tutorials page from a template by filling in a list of all the demos
# found in the `pages/` directory
pages/tutorials.rst pages/how-to.rst &: notebooks make_notebook_pages.py
	python3 make_notebook_pages.py

all: notebooks pages/tutorials.rst pages/how-to.rst
	nikola build

clean:
	rm pages/*.ipynb executed-demos/*.ipynb
	nikola clean
