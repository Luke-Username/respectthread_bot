#!/bin/bash
# Script to read in test inputs and feed them into the program.
# It also compares the expected output to the program's actual output.
# It tracks the tests that fail with a name and time stamp in test_results.txt.
# For every test that fails, it writes the difference beetween the expected output and actual output in diff_log.txt.
# It assumes two things are in the same directory as it:
#   1. A Python script, test_output_given_text.py, that uses the functions being tested.
#   2. A folder of test cases, test-cases/*

# The folder holding the test cases.
testcases="test-cases/*"

# To give a time stamp for each test run.
datetime=`date +"%Y-%m-%d %T"`

# File that logs the results of each test run.
test_results_file="test_results.txt"

# File that logs the difference between the expected output and actual output in each case.
diff_log_file="diff_log.txt"

# Flag for if a test fails
test_failed=false

process_input_file() {
    # $1 is the input file name given as the 1st argument. 
    # This line calls a Python script and gives it a file to look at

    # Make sure the test output file exists
    local output_file="temp_output_file.txt"
    touch "$output_file"

    # Run Python code and write its output into a temporary file 
    # so it can be compared to the expected output
    (python3 test_output_given_text.py $1) > "$output_file"
    #python3 test_output_given_text.py $1

    # Get the expected output file
    local expected_output=`echo "$1" | cut -d '.' -f1`
	expected_output+=".ou.txt"

    # Get the difference between the expected output and real output
    local output_diff=$(diff "$expected_output" "$output_file")
    local test_name=`echo "$1" | cut -d '/' -f3`
    if [ "$output_diff" == "" ]
    then
	echo "($datetime) TEST $test_name: GOOD" >> "$test_results_file"
        echo "TEST $test_name: GOOD"
    else
        test_failed=true
        echo "($datetime) TEST $test_name: BAD" >> "$test_results_file"
        echo "TEST $test_name: BAD"
        echo "$test_name:" >> "$diff_log_file"
        echo "$output_diff" >> "$diff_log_file"
        echo "" >> "$diff_log_file"
    fi
}

# Add a banner to the test results to label the date and time of testing
echo "##################################################" >> "$test_results_file"
echo "TEST RESULTS ($datetime)" >> "$test_results_file"
echo "##################################################" >> "$test_results_file"
echo "" >> "$test_results_file"

# Add a banner to the difference log to label the date and time of testing
echo "##################################################" >> "$diff_log_file"
echo "DIFFERENCE LOG ($datetime)" >> "$diff_log_file"
echo "##################################################" >> "$diff_log_file"
echo "" >> "$diff_log_file"

# Run the tests
echo "Test run ($datetime)"
for testtype in $testcases
do
    # If it's a directory, move into it
    if [ -d "$testtype" ]
    then
        #testtype_name=`echo "$testtype" | cut -d '/' -f2` # Extract the folder name from the directory
        testtype_name=`echo "$testtype"`
        echo "Testing $testtype_name"  # Print what the script is currently testing
        test_cases="$testtype/*"
        for case in $test_cases
        do
            # If its a directory, move into it
   	    if [ -d "$case" ]
   	    then
                #echo $case
                files="$case/*"
                for file in $files
                do
                    # If the file extension matches the test input format, 
                    # call a function to process the file
                    if [ "${file: -7}" == ".in.txt" ]
                    then
                        process_input_file "$file"
                    fi
                done
            fi
            #break
        done
    fi
    #break
done

if [ "$test_failed" = true ] ; then
    echo "One or more tests have failed! Be sure to check that RegExs are correct and links are up-to-date."
fi