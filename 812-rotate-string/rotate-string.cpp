class Solution {
public:
    bool rotateString(string s, string goal) {
        int n=s.length();
        string news=s;
        for(int i=0;i<n;i++)
        {
            if(news==goal)
            {
                return true;
            }
            char a=news[0];
            news.erase(0,1);
            news.push_back(a);
        }
        return false;   
    }
};