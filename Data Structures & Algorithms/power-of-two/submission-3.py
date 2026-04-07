class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #  Model Bit Manipulation - II
        return n > 0 and n & (n-1) == 0


        