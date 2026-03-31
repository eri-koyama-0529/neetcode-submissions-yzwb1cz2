class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = {5:0, 10:0, 20:0}

        for bill in bills:
            money[bill] += 1

            if bill == 10:
                if money[5] <= 0:
                    return False
                money[5] -= 1

            elif bill == 20:
                if money[5] > 0 and money[10] > 0:
                    money[5] -= 1
                    money[10] -= 1
                elif money[5] >= 3:
                    money[5] -= 3
                else:
                    return False
        
        return True
        