def run_tests(test_suite, fn):
    """
    Runs a list of test cases.

    test_suite: list of dicts
        Each dict must have:
        - name: str, name of the test
        - fn: callable, function to test
        - args: list, positional arguments for the function
        - expected: expected output
    """
    for case in test_suite:
        args = case["args"]
        expected = case["expected"]

        try:
            result = fn(*args)
            status = "PASS" if result == expected else "FAIL"
        except Exception as e:
            result = f"ERROR: {e}"
            status = "ERROR"

        print(f"{status} | {case['name']} | got={result} expected={expected}")