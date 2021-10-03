#https://leetcode.com/problems/ransom-note/submissions/
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''l1 = []
        l2 = []
        for i in ransomNote:
            l2.append(i)
        for i in magazine:
            l1.append(i)
        li_dif = [i for i in l1 + l2 if i not in l1 or i not in l2]
        if(len(li_dif) == 0):
            return "true"
        else:
            return "false"'''
        d1 = Counter(magazine)
        d2 = Counter(ransomNote)
        for i in d2:
            if d2[i] > d1[i]:
                return False
        return True
