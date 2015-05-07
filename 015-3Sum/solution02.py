#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 6, 2015
# Question: 015-3Sum
# Link:     https://leetcode.com/problems/3sum/
# ==============================================================================
# Given an array S of n integers, are there elements a, b, c in S such that 
# a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# 
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
# The solution set must not contain duplicate triplets.
# 
#     For example, given array S = {-1 0 1 2 -1 -4},
# 
#     A solution set is:
#     (-1, 0, 1)
#     (-1, -1, 2)
# ==============================================================================
# Method: Two pointers
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Note: 
# 1. Refer to Two Pointers methods in LeetCode Question #001-Two-Sum.
# 2. Annoying to remove duplication.
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        stack = []
        nums.sort()
        size = len(nums)
        
        i = 0
        while i < size - 2:
            low = i + 1
            high = size - 1
            while low < high:
                if nums[i] + nums[low] + nums[high] == 0:
                    stack.append((nums[i], nums[low], nums[high]))
                    while low < high and nums[low] == nums[low+1]: low += 1
                    while low < high and nums[high] == nums[high-1]: high -= 1
                    low += 1
                    high -= 1
                elif nums[i] + nums[low] + nums[high] > 0:
                    high -= 1
                else:
                    low += 1
            while i < size-2 and nums[i] == nums[i+1]: i += 1
            i += 1
        return stack

if __name__ == '__main__':
    test0 = [-1,0,1,2,-1,-4]
    test1 = [-14,-10,-1,8,-8,-7,-3,-2,14,10,3,3,-1,-15,6,9,-1,6,-2,-6,-8,-15,8,-3,-14,5,-1,-12,-10,-5,-9,-8,1,-3,-15,0,-3,-11,6,-11,7,-6,7,-9,-6,-10,7,1,11,-10,10,-12,-10,3,-7,-9,-7,7,-14,-9,10,14,-2,-4,-4,-10,3,1,-14,-6,5,8,-4,-11,14,-3,-6,-2,13,13,3,0,-14,8,10,-14,6,11,1,7,-13,-4,6,0,-1,10,-3,-13,-4,-2,-11,8,-8]
    test2 = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    test3 = [4,-8,-9,9,10,-3,13,12,9,8,9,5,-4,-8,7,-12,-14,-11,-10,-6,2,7,-3,9,-8,9,-2,11,3,8,7,-8,-15,13,9,3,-5,-1,0,-11,-7,-5,1,4,-6,-7,-1,-13,-11,4,-4,-2,-12,0,-7,-5,-13,6,13,-3,-9,5,-4,-8,3,-10,10,5,5,-13,1,13,-11,-13,-6,-10,-4,1,-8,-8,-10,-4,6,-6,3,14,-4,5,-3,-5,9,4,-15,-9,3,-4,-4,-10,8,8,-8,-5,-2,-11]
    test4 = [-5,14,1,-2,11,11,-10,3,-6,0,3,-4,-9,-13,-8,-7,9,8,-7,11,12,-7,4,-7,-1,-5,13,1,-2,8,-13,0,-1,3,13,-13,-1,10,5,1,-13,-15,12,-7,-13,-11,-7,3,13,1,0,2,1,11,10,8,-8,1,-14,-3,-6,-12,12,0,6,2,2,-9,-3,14,-1,-9,14,-4,-1,8,-8,7,-4,12,-14,3,-9,2,0,-13,-13,-1,3,-12,11,4,-9,8,11,5,-5,-10,3,-1,-11,-13,5,-12,-10,11,11,-3,-5,14,-13,-4,-5,-7,6,2,-13,0,8,-3,4,4,-14,2]
    test5 = [11,-8,9,-6,-10,14,-5,-10,2,-1,-14,-13,-5,9,-5,-12,9,5,-1,-4,-14,5,-11,3,6,-7,2,-14,9,-6,-8,-2,-7,8,7,-2,7,9,3,-14,-14,5,-12,-4,-9,-1,-8,7,11,-2,-11,4,-11,-15,-7,10,-7,10,4,10,11,11,-7,-11,4,7,2,-12,1,12,-10,2,2,-15,6,1,-1,13,-7,-12,-4,-11,7,0,-11,-15,-12,-10,2,7,-15,-2,3,-15,-6,14,-1,11,-13,-15,9,14,-5,-12,-15,-14,4,-9,6,5,-6,-13,9]
    test6 = [-6,14,-11,7,-5,-8,12,-13,-3,-14,7,0,-7,-15,-5,-9,-13,-7,-5,9,8,-13,-6,-8,-12,7,-10,11,8,-14,12,9,-15,-14,1,-5,-7,-10,-10,5,-9,12,12,-1,12,14,-2,-15,-8,0,9,7,2,10,14,-3,2,11,-6,-13,12,13,11,5,14,-11,7,14,-6,12,-4,-7,9,-7,-1,-1,-8,4,-9,-9,-11,-15,5,6,10,4,11,-10,-8,12,-8,-10,10,11,2,9,-15,-14,0,-13,14,11,-5,0,-11,1,6,-12]
    test7 = [-5,1,-10,2,-7,-13,-3,-8,2,-15,9,-3,-15,13,-6,-10,5,6,11,1,13,-12,14,6,11,4,13,-14,0,11,1,10,-11,6,-11,-10,8,2,-3,-13,-6,-9,-9,-6,11,-8,-9,1,13,9,9,3,13,0,-6,1,-10,-15,3,5,3,11,-8,0,2,-11,5,-13,6,9,-11,7,8,-13,8,4,-6,14,13,-15,1,7,-5,-1,-7,5,7,-2,-3,-13,10,7,13,9,-8,-8,13,12,-6,4,7,-10,-12,-8,-8,11,11,-6,3,9,-14,-11,2,-4,-5,10,8,-13,-7,12,-10,10]
    test8 = [0,0,0]
    test9 = [1,1,1]
    res = Solution().threeSum(test9)
    print res, len(res), len(set(res))