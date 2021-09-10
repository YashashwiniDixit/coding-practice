class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=nums[0]
        n=len(nums)
        for i in range(0,n):
            #print(i)
            for j in range(i+1,n+1):
               # print(j)
                sum=0
                for k in range(i,j):
                   # print(k)
                    sum+=nums[k]
                if max<sum:
                    max=sum
        return max
                    
        #https://leetcode.com/problems/maximum-subarray
        #first try not optimized
