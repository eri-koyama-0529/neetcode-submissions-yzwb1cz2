class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_all = 1
        count_zero = 0
        for n in nums:
            if n != 0:
                product_all *= n
            else:
                count_zero += 1

        res = []
        if count_zero > 1:
            for _ in range(len(nums)):
                res.append(0)
        # print(product_all)
            return res

        if 0 in nums:
            for n in nums:
                # print(res)
                if n == 0:
                    res.append(product_all)
                else:
                    res.append(0)
        else:            
            for n in nums:
                res.append(product_all//n)
        return res