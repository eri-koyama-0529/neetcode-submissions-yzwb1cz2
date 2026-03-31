class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        base = ord('A')-1
        res = []
        n = columnNumber

        while n > 0:
            rest = n % 26
            n //= 26
            print(n)
            print(rest)
            print(chr(rest+base))
            print()
            
            res.append(chr(base+rest))
            if n == 26:
                res.append(chr(base+n))
                n %= 26
        res.reverse()
        return ''.join(res)