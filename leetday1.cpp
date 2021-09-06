//https://leetcode.com/problems/contains-duplicate/
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> s;
 
        bool dupFound = false;
        
        for (int i = 0; i<nums.size(); i++)
        {
            if (s.find(nums[i]) != s.end())
            {
                dupFound = true;
            }
            else
                s.insert(nums[i]);
        }
        return dupFound;
    }
};
