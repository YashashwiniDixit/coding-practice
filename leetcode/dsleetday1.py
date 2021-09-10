#https://leetcode.com/problems/contains-duplicate/
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = dict.fromkeys(nums,0)
        for i in nums:
            n[i]+=1
            if n[i]>=2:
                print(n[i])
                return True
            else:
                continue
        return False
