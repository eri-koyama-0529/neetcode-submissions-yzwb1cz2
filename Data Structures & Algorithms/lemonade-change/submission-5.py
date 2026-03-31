class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Model Answer:  Iteration - II
        five, ten = 0, 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                five, ten = five-1, ten+1
            # 以下は$20の時、＄10が一枚以上あれば、$5と$10でおつり
            elif ten > 0:
                five, ten = five-1, ten-1
            else:
                five -= 3
            if five < 0:
                return False
        return True
        