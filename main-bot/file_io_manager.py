
# Modules
import os           # To check if a file exists

def write_to(filename: str, content: str):
    with open(filename, "a") as f:
        f.write(content)

def get_content_as_list(filename: str):
    content = []
    if not os.path.isfile(filename):
        content = []
    else:
        with open(filename, "r") as f:
            content = f.read().split("\n")
    return content
