class Solution:
    def tribonacci(self, n: int) -> int:
        # Model Answer: Dynamic Programming (Space Optimized)
        t = [0, 1, 1]

        if n <= 2:
            return t[n]
        
        for i in range(3, n+1):
            t[i%3] = sum(t)
        return t[n%3]
        