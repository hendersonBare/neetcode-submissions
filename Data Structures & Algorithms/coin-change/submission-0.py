class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #we always have atleast 1 coin
        #it is not always possible to form the target amount
        #the amount itself is non-negative
        #since we only want to find the minimum number of coins,
        #we can use a memoized DP solution instead of backtracking
        #we will populate the array with amount+1 since we will always 
        #be taking the min and never sum to more than amount
        #and we are using 0-based indexing in python

        memo = [amount+1] * (amount+1)
        memo[0] = 0
        for i in range(amount+1):
            for c in coins:
                if i-c >= 0:
                    memo[i] = min(memo[i],1+memo[i-c])
        if memo[-1] == amount+1:
            return -1
        return memo[-1]
