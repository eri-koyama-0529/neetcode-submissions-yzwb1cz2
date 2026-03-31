class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # Model Answer: Iteration
        res = []
        n = columnNumber

        while n > 0:
            n -= 1
            offset = n % 26
            res += chr(ord('A')+offset)
            n //= 26

        return ''.join(reversed(res))