class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        確認
        ・[]->ない
        方針
        ・pivot => 真ん中
        →小さい＋同じ＋大きい
        ↑各区分が1になるまで繰り返す
        """
        length = len(nums)
        if length <= 1:
            return nums
        
        pivot = nums[length//2]
        small, middle, large = [],[],[]
        for n in nums:
            if n < pivot:
                small.append(n)
            elif n == pivot:
                middle.append(n)
            else:
                large.append(n)
        
        return self.sortArray(small) + middle + self.sortArray(large)
