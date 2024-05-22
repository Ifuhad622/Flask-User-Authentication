#!/usr/bin/python3
import os
from tempfile import mkstemp
from shutil import move
from urllib.parse import unquote

# Path to the affected file
file_path = "/usr/local/lib/python3.8/dist-packages/flask_login/utils.py"

# Read the contents of the file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Modify the contents of the file
for i, line in enumerate(lines):
    if "from werkzeug.utils import url_decode" in line:
        lines[i] = "from urllib.parse import unquote\n"
    elif "decoded_url = url_decode(url)" in line:
        lines[i] = "decoded_url = unquote(url)\n"

# Write the modified contents back to the file
with open(file_path, 'w') as file:
    file.writelines(lines)

print("File '{}' has been modified successfully.".format(file_path))

