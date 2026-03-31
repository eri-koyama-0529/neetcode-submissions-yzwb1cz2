class Solution:
    def romanToInt(self, s: str) -> int:
        length = len(s)
        r_to_n = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0

        for i in range(length-1):
            if r_to_n[s[i]] < r_to_n[s[i+1]]:
                res -= r_to_n[s[i]]
            else:
                res += r_to_n[s[i]]
        
        return res + r_to_n[s[length-1]]
