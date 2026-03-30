class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        citizen = set()
        candidate = {}

        for a, b in trust:
            citizen.add(a)
            if a in candidate:
                del candidate[a]
            
            if b not in citizen:
                res = b
                candidate[b] = candidate.get(b,0)+1

        if len(candidate) == 1:
            if candidate[res] == (n-1):
                return b
        return -1
        