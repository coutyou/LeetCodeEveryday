class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        pre = None
        cnt = 1
        for c in preorder:
            if c == ",":
                cnt -= 1
                if cnt < 0:
                    return False
                if pre != "#":
                    cnt += 2
            pre = c
        cnt -= 1
        if cnt < 0:
            return False
        if pre != "#":
            cnt += 2
        return cnt == 0