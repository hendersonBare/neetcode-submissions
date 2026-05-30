class Solution:
    def climbStairs(self, n: int) -> int:
        result = 1 #case where the solution is all 1s
        num_of_twos = n // 2
        i = 1
        while(i <= num_of_twos):
            places = n - i
            if(places != i):
                result += math.comb(places, i)
            else:
                result +=1
            i+=1
        return result