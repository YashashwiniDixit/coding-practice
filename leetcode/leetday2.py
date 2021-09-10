class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference in visited:
                return [visited[difference], index]
            else:
                visited[number] = index
                #https://leetcode.com/problems/two-sum
