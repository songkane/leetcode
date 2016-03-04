"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""



class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        k = 0
        j = len(nums)
        if j == 0:
            return False
        for i in nums:
            if i in d:
                return True
                break
            else:
                d[i]=1
                k = k+1
                if k == j:
                    return False
                    break
