#-*- conding: utf-8 -*-
"""
罗马数字的表示为：{'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1} 
左边比右边小为减，不存在二意，也不存在两种表达法
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        罗马数字的表示为：{'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1} 左边比右边小为减，
        不存在二意，也不存在两种表达法
        """
        dic = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        result = dic[s[-1]]        
        for i in range(0,len(s) - 1):
            if dic[s[i]] >= dic[s[i+1]] :
                result = result + dic[s[i]]
            else :
               result = result - dic[s[i]]             
        return result