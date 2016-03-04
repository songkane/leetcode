"""
Given an array of size n, find the majority element. The majority element is the element that appears more than [] n/2 ] times.
You may assume that the array is non-empty and the majority element always exist in the array.

nums=[1,2,3,2,1,4,2,2,2,3,4,2,2,2,]
n = len(nums)
for i in nums:
	if nums.count(i)>(n/2.0):
		break
print i
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        d = {}
        for i in nums:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        for j in d:
            if d[j]>(n/2.0):
                return j
                break
