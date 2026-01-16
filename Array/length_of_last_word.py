testing_suite = [
{
    "name": "Length of Last Word #1",
    "args": ["Hello World"],
    "expected": 5
},
{
    "name": "Length of Last Word #2",
    "args": ["   fly me   to   the moon  "],
    "expected": 4
},
{
    "name": "Length of Last Word #3",
    "args": ["luffy is still joyboy"],
    "expected": 6
}]

def lengthOfLastWord(s):
        count = 0
        firstLetterFound = False
        for i in s[::-1]:
            if i.isalpha():
                firstLetterFound = True
                count += 1
            elif firstLetterFound:
                return count
        return count


if __name__ == "__main__":
    from test_framework.test_runner import run_tests
    run_tests(testing_suite, lengthOfLastWord)