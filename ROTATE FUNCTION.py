# PROBLEM STATEMENT:-
# You are given an integer array nums of length n. Return maximum length of Rotation Function.

# LINK:-
# https://leetcode.com/problems/rotate-function/

# CODE:-
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        sums = c_sum = sum(idx * ele for idx, ele in enumerate(nums))
        s = sum(nums)
        n = len(nums)
        while nums:
            c_sum += s - nums.pop() * n
            sums = max(c_sum, sums)
        return sums

# LOGIC USED:-
# Dynamic Programming

# TIME COMPLEXITY:-
# O(n)
