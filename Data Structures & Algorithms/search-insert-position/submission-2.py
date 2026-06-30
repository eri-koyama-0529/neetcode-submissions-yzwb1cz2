class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        方針
        ・二分探索→見つかるか
        ・見つからなかった→最後のmidより大きい→mid+1 ,小さい→mid
        [1,2,4,6,7] ,5
        """

        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return mid if target < nums[mid] else mid+1