#https://leetcode.com/problems/array-nesting/
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        l1=[]
        for i in range(len(nums)):
            if i not in l1:
                k=1
                x=nums[i]
                j=i
                while x!=i:
                    l1.append(x)
                    j=nums[j]
                    x=nums[j]
                    k+=1

                l.append(k)
        print(l)
        l.sort()
        return l[-1]
            
            
        
