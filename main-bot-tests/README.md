Unit tests and test cases to make sure the bot functions properly after changes are made to it.
If a test fails, it may require investigation.
The scripts to run the tests are explained below.

---

### Scripts to run tests

```
./run_unit_tests.sh
```

A simple script that runs all Python unit tests in the `unit-tests` folder.

```
./run_test_cases.sh
```

A script that feeds text files into `test_output_given_text.py`
and compares the output to the expected output.
This will be slow because it has to connect and disconnect to the database for each test case.
Inputs and expect outputs can be found in the `test-cases` folder.


```
./run_all_tests.sh
```

A simple script that runs `run_unit_tests.sh` then `run_test_cases.sh`. 
It's here so people only have to run one script to run all tests.
