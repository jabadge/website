import json
import pathlib
from extract_title import extract_title

# Get the template text for the tutorials page
template_filename = 'pages-sources/tutorials.rst'
with open(template_filename, 'r') as template_file:
    template = template_file.read()

text = "\n"

# Find all the demos in the `pages/` directory, sort them, extract the title of
# each one, and put it in the text we'll insert into the template along with
# right reST incantation to add a hyperlink
demo_filenames = sorted(list(pathlib.Path('pages/').glob('demos-*.ipynb')))
for filename in demo_filenames:
    with open(filename, 'r') as tutorial_file:
        tutorial = json.load(tutorial_file)

    title = extract_title(tutorial)
    text += f"    `{title} </{filename.stem}/>`_\n\n"

# Stuff the list of tutorial links into the template and write the result to
# the tutorials page
output_filename = 'pages/tutorials.rst'
with open(output_filename, 'w') as output_file:
    output_file.write(template.format(text))
