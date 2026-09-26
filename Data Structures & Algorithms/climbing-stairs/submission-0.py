class Solution:
    def climbStairs(self, n: int) -> int:

        prev = 1
        current = 1

        for i in range(1,n):
            nextV = prev + current 
            prev, current = current, nextV
            
        return current
        