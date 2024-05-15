"""20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

    Input: s = "()"
    Output: true

Example 2:

    Input: s = "()[]{}"
    Output: true

Example 3:

    Input: s = "(]"
    Output: false

"""
from collections import deque

def valid_parenthesis(s:str)-> bool:
    stack = deque()
    closeToOpen = {
        ")":"(",
        "]":"[",
        "}":"{"
    }

    for char in s:
        if char in closeToOpen:
            if stack and stack[-1] == closeToOpen[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    if not stack:
        return True
    else:
        return False



if __name__ == "__main__":
    testCases = [
        "()",
        "()[]{}",
        "(]",
        "]"
    ]
    for testCase in testCases:
        print(valid_parenthesis(testCase))