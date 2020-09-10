
# Find all of the icepack demos by searching the `demo` directory of icepack
# for anything that ends with `.ipynb` and isn't a directory and sort them
DEMO_FILES:=$(shell find ${ICEPACK}/demo -not -path '*/\.*' -type f -name '*\.ipynb' | sort)

# Make a `notebooks` target containing all of the imported, executed demos
notebooks: $(patsubst ${ICEPACK}/demo/%.ipynb,pages/%.ipynb,$(DEMO_FILES))

.PRECIOUS: executed-demos/%.ipynb

# To get any executed demo from its source in icepack, call `jupyter nbconvert`
executed-demos/%.ipynb: ${ICEPACK}/demo/%.ipynb
	jupyter nbconvert \
	    --to ipynb \
	    --execute \
	    --ExecutePreprocessor.timeout=24000 \
	    --output-dir=./executed-demos \
	    --output=`basename $@` \
	    $<

# To get any demo page from an executed demo, call `nikola new_page`, extract
# the title of the demo from its raw source, and import it
pages/%.ipynb: executed-demos/%.ipynb
	nikola new_page \
	    --format ipynb \
	    --title="$$(python3 extract_title.py $<)" \
	    --import=$< \
	    $@

.PHONY: clean
clean:
	rm pages/*.ipynb executed-demos/*.ipynb
	nikola clean
