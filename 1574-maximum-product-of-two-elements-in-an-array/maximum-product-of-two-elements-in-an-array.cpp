class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int a=(nums[0]-1)*(nums[1]-1);
        for(int i=0;i<nums.size();i++)
        {
            for(int j=1;j<nums.size();j++)
            {
                int b=(nums[i]-1)*(nums[j]-1);
                {
                    if(i!=j)
                    {
                        if(b>a)
                        {
                            a=b;
                        }
                    } 
                }
            }
        }
        return a;
    }
};