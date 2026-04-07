class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #  Model Bit Manipulation - I
        return n > 0 and n & (-n) == n


        