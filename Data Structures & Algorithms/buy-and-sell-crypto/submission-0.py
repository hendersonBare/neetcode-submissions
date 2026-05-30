class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left_pointer = 0
        right_pointer = 1
        while(right_pointer < len(prices) and left_pointer < right_pointer):
            price_diff = prices[right_pointer] - prices[left_pointer]
            if(price_diff > max_profit):
                max_profit = price_diff
            elif (price_diff < 0):
                left_pointer = right_pointer
            right_pointer+=1
        return max_profit