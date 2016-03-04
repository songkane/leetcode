#-*- coding: utf-8 -*-
'''
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
'''
n=1
i=0
while n:
	i = i + n%2
	n=n>>1
print i