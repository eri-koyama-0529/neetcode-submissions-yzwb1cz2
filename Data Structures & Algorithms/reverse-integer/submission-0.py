class Solution:
    def reverse(self, x: int) -> int:
        """
        確認
        ・負の整数：-123 -> -321
        方針
        ・res
        ・x:10で割った商、　res+= 10で割ったあまり
        ・resは毎回10倍
        """
        res = 0
        is_Minus = 1

        if x < 0:
            is_Minus = -1
            x *= -1

        while x != 0:
            digit = x % 10
            x = x // 10
            res = res * 10 + digit
        
        res *= is_Minus

        if res < (-1)*2**31 or (2**31)-1 < res:
            return 0

        return res
        