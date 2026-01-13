testing_suite = [
{
    "name": "TwoSum #1",
    "args": [[2, 7, 11, 15],9],
    "expected": [0, 1]
},
{
    "name": "TwoSum #1",
    "args": [[3, 2, 4],6],
    "expected": [1,2]
},
{
    "name": "TwoSum #1",
    "args": [[3, 3],6],
    "expected": [0, 1]
}]


def twoSum(nums, target):
    seen = {}  # number -> index

    for i, num in enumerate(nums):
        need = target - num

        if need in seen:
            return [seen[need], i]

        seen[num] = i


if __name__ == "__main__":
    from test_framework.test_runner import run_tests
    run_tests(testing_suite, twoSum)