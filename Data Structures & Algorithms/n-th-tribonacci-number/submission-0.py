class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1
        
        T_n , T_n1, T_n2 = 0, 1, 1
        res = 0

        for i in range(3, n+1):
            res = T_n + T_n1 + T_n2
            T_n = T_n1
            T_n1 = T_n2
            T_n2 = res
        
        return res
        