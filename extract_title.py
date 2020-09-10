import sys
import json

def extract_title(notebook):
    cells = notebook['cells']
    for cell in cells:
        if cell['cell_type'] == 'markdown':
            for line in cell['source']:
                line = line.lstrip().rstrip()
                words = line.split(' ')
                if words[0] == '#':
                    return ' '.join(words[1:])

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, 'r') as notebook_file:
        notebook = json.load(notebook_file)

    title = extract_title(notebook)
    print(title)
