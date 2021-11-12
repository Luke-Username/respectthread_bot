#!/bin/bash

# The script is given the test case folder as input
if [ "$#" -ne 1 ] || ! [ -d "$1" ]; then
    echo "Usage: $0 DIRECTORY" >&2
    exit 1
fi

directory="$1*"
input_file=""
expected_output_file=""
for file in $directory
    do
        # If the file extension matches the test input format
        if [ "${file: -7}" == ".in.txt" ]
        then
            input_file="$file"
        elif [ "${file: -7}" == ".ou.txt" ]
        then
            expected_output_file=$file
        fi
    done

# Make sure the test output file exists
output_file="temp_output_file.txt"
touch "$output_file"

# Run Python code and store what it prints
output=$(python3 test_output_given_text.py $input_file)

# Write the output to the temporary file
echo "$output" > "$output_file"

# Get the difference between temp file and the expected output
output_diff=$(diff "$expected_output_file" "$output_file")

# Print the results
printf "### output:\n"
printf "$output"
printf "\n"
printf "### expected output:\n"
cat "$expected_output_file"
printf ""
printf "### diff:\n\n"
printf "$output_diff"
printf "\n"
