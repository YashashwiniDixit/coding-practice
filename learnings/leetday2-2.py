class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, i = m-1, n-1, len(nums1)-1
        while p1 > -1 and p2 > -1:
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
            i  -= 1
        while p2 > -1:
            nums1[i] = nums2[p2]
            i -= 1
            p2 -= 1
#https://leetcode.com/problems/merge-sorted-array
