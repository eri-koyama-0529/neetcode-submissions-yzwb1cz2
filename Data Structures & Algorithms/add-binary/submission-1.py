class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        c = 0
        len_a, len_b = len(a), len(b)

        if len_a < len_b:
            for i in range(len_b - len_a):
                a = '0' + a
        else:
            for i in range(len_a - len_b):
                b = '0' + b

        for i in range(max(len_a, len_b)-1,-1,-1):
            temp = int(a[i]) + int(b[i]) + c
            if temp < 2:
                res = str(temp) + res
                c = 0
            else:
                c = 1
                res = str(temp%2) + res
        
        return res if c == 0 else str(c) + res