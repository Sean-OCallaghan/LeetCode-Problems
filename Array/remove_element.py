testing_suite = [
{
    "name": "Remove Element #1",
    "args": [[3, 2, 2, 3],3],
    "expected": [2, 2]
},
{
    "name": "Remove Element #2",
    "args": [[3, 2, 4],6],
    "expected": [3,2,4]
},
{
    "name": "Remove Element #3",
    "args": [[3, 3],6],
    "expected": [3, 3]
}]


def removeElement(nums, val):
     for i in range(nums.count(val)):
            nums.remove(val)
        
     return nums


if __name__ == "__main__":
    from test_framework.test_runner import run_tests
    run_tests(testing_suite, removeElement)