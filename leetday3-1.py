//https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        nums1.sort()
        nums2.sort()
        m = len(nums1)
        n = len(nums2)
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j+= 1
            else:
                l.append(nums2[j])
                j += 1
                i += 1
        return l
