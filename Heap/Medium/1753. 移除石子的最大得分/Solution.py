class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        if a+b <= c:
            return a+b
        elif a+c <= b:
            return a+c
        elif b+c <= a:
            return b+c
        return (a+b+c)//2
