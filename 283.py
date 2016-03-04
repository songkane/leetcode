'''Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''





nums= [1,23,4,1,4,0,9,0,5,0]
j = []
k=0
for i in nums:
    if i == 0:
        j.append(k)
    k=k+1
for n in j[::-1]:
    nums.pop(n)
    nums.append(0)
print nums
            
                