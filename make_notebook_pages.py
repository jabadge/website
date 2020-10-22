import json
import pathlib
from extract_title import extract_title

def make_pages(page_type):
    template_filename = f"pages-sources/{page_type}.rst"
    with open(template_filename, "r") as template_file:
        template = template_file.read()

    text = "\n"

    # Find all the demos in the `pages/notebooks/` directory, sort them,
    # extract the title of each one, and put it in the text that we"ll insert
    # into the template along with the right ReST incantation to add a link
    directory = f"pages/notebooks/{page_type}"
    filenames = sorted(pathlib.Path(directory).glob("*.ipynb"))
    for filename in filenames:
        with open(filename, "r") as notebook_file:
            notebook = json.load(notebook_file)

        title = extract_title(notebook)
        text += f"    `{title} </notebooks/{page_type}/{filename.stem}/>`_\n\n"

    # Stuff the list of notebook links into the template and write the result
    # to the corresponding page
    output_filename = f"pages/{page_type}.rst"
    with open(output_filename, "w") as output_file:
        output_file.write(template.format(text))


# Make the page for both tutorials and how-to guides
if __name__ == "__main__":
    for page_type in ["tutorials", "how-to"]:
        make_pages(page_type)
