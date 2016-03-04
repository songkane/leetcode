"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""
numbers=[2,7,2,2,7,7,15]
target=22
d = {}
for i,v in enumerate(numbers):
	if target - v in d:
		print  d[target-v]+1,i+1
		break
	d[v]=i
	print (v,i)
