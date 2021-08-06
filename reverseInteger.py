class Solution:
    def reverse(self, x: int):
        if x < 0:
            temp = -int(str(x)[1:][::-1])
        else:
            temp = int(str(x)[::-1])
        if temp > 2**31-1 or temp < -2**31: return 0
        else: return temp