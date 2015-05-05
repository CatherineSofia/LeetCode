#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 1, 2015
# Question: 202-Happy-Number
# Link:     https://leetcode.com/problems/happy-number/
# ==============================================================================
# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with 
# any positive integer, replace the number by the sum of the squares of its 
# digits, and repeat the process until the number equals 1 (where it will stay), 
# or it loops endlessly in a cycle which does not include 1. Those numbers for 
# which this process ends in 1 are happy numbers.

# Example: 19 is a happy number

# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# ==============================================================================

class Solution:
    # @param {integer} n
    # @return {boolean}
    def __init__(self):
    	self.loop = []

    def isHappy(self, n):
    	if n == 1:
    		return True
    	elif n in self.loop:
    		return False
    	else:
    		self.loop.append(n)
    		return self.isHappy(sum([int(c)**2 for c in str(n)]))
