#include <map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> hash;
        vector<int> result;
        for (int i=0; i < nums.size(); i++) {
            int diff = target - nums[i];
            
            if (hash.find(diff) != hash.end()) {
                result.push_back(hash[diff] + 1);
                result.push_back(i + 1);
                return result;
            }
            else {
                hash[nums[i]] = i;
            }
        }
        return result;
    }
};