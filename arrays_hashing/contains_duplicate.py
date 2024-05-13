"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109

url:  https://leetcode.com/problems/contains-duplicate/description/
@iancmckee
"""
from typing import List

def contains_duplicates(nums: List[int]) -> bool:
    s = set(nums)
    return len(s) != len(nums)

    # Alternative Solution - Neetcode
    # hashset = set()
    # for num in nums:
    #     if num in hashset:
    #         return True
    #     else:
    #         hashset.add(num)
    # return False



if __name__ == '__main__':
    myLists= [[1,2,3,1],[1,2,3,4],[1,1,1,3,3,4,3,2,4,2]]
    for list in myLists:
        print(contains_duplicates(list))
