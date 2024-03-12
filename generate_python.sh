#!/bin/bash

create_folder() {
    if [ ! -d "$folder" ]; then
        mkdir -p "$folder"
        echo "Folder $folder created."
    fi
}


folder="$1"

create_folder

if [ -e "$folder/solution.py" ]; then
    echo "Error: File already exists."
    exit 1
fi

# Generate starter code and write it to the file
cat << EOF > "$folder/solution.py"
### PATH CONFIGURATION FOR IMPORTING MODULES FROM ROOT DIR
import sys
from os.path import dirname
from pathlib import Path
p = Path(__file__).parents[2]
sys.path.append(dirname(p))
from utils.input_tuple_int import parse_tuple_int
### PATH CONFIGURATION FOR IMPORTING MODULES FROM ROOT DIR


if __name__ == "__main__":
EOF

cat << EOF > "$folder/readme.md"
# $folder
EOF

echo "Python file solution.py created successfully in $folder."
