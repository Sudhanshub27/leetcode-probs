class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int sum=numBottles;
        int temp=numBottles;
        while(temp>=numExchange)
        {
            int newbottles=temp/numExchange;
            sum=sum+newbottles;
            temp=newbottles+(temp%numExchange);
        }
       return sum;
    }
};