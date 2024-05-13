"""125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.
Example 3:

    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
import re


def valid_palindrome(s: str) -> bool:
    # Strip all non-alphanumeric values - \W = [^a-zA-Z0-9_]
    strippedString = re.sub('[^a-zA-Z0-9]+', '', s)
    strippedString = strippedString.lower()
    #assign left and right pointers
    r = len(strippedString) - 1
    l = 0
    #watch out for infinite loops
    while r > l:
        if strippedString[l] == strippedString[r]:
            r -= 1
            l += 1
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    my_tests = [
                "A man, a plan, a canal: Panama",
                "race a car",
                " ",
                "ab_a"
                ]
    for test in my_tests:
        print(valid_palindrome(test))
