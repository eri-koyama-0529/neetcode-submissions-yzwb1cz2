class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def update_lists(strs):
            res = []
            for s in strs:
                sorted_s = sorted(s)
                res.append((''.join(sorted_s), s))
            
            return res
        
        def check_anagrams(lists):
            dic = {} # res["aba"] = ["aab", "aba"]
            keys = []
            for sorted_s, s in lists:
                if sorted_s in dic:
                    dic[sorted_s].append(s)
                else:
                    keys.append(sorted_s)
                    dic[sorted_s]=[s]
            
            res = []
            for k in keys:
                res.append(dic[k])
            print(res)
            return res
    
        # print(update_lists(strs))
        lists = update_lists(strs)
        return check_anagrams(lists)
