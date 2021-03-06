#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 2, 2015
Question: 169-Majority-Element
Link:     https://leetcode.com/problems/majority-element/
==============================================================================
Given an array of size n, find the majority element. The majority element is 
the element that appears more than floor(n/2) times.

You may assume that the array is non-empty and the majority element always 
exist in the array.
==============================================================================
Method: randomly pick up a number and figure out whether it appears more than
floor(n/2) times
Time Complexity: O(n)
Space Complexity: O(1)
Reference: http://www.cnblogs.com/fanyabo/p/4178993.html
==============================================================================
"""

import random

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        size = len(nums)
        while 1:
            idx = random.randint(0,size-1)
            if nums.count(nums[idx]) > size/2:
                return nums[idx]
