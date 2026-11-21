class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, int> m;
        bool has=false;
        for(int i=0;i<nums.size();++i)
        {
            m[nums[i]] += 1;

            if(m[nums[i]] > 1)
            {
                has = true;
            }             
        }
        return has;
    }
};
