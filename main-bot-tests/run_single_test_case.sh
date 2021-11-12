#!/bin/bash

# The script is given the test case folder as input
if [ "$#" -ne 1 ] || ! [ -d "$1" ]; then
    echo "Usage: $0 DIRECTORY" >&2
    exit 1
fi

input=""
expected_output=""
for file in $1
    do
        # If the file extension matches the test input format
        if [ "${file: -7}" == ".in.txt" ]
        then
            $input=$file
        elif [ "${file: -7}" == ".ou.txt" ]
        then
            $expected_output=$file
        fi
    done

# Make sure the test output file exists
local output_file="temp_output_file.txt"
touch "$output_file"

# Run Python code and write its output into a temporary file 
# so it can be compared to the expected output
output=$(python3 test_output_given_text.py $input)

$output > "$output_file"

output_diff=$(diff "$expected_output" "$output_file")

echo "$output"
echo "$output_diff"
