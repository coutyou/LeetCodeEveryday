class Solution:
    def isValid(self, s: str) -> bool:
        # 空字符串
        if not s:
            return True
        hash_ = {')':'(', '}':'{', ']':'['}
        stack = []
        for c in s:
            # 左边
            if c not in hash_:
                stack.append(c)
            else:
                # 栈空
                if not stack:
                    return False
                # 不匹配
                if stack[-1] != hash_[c]:
                    return False
                # 匹配
                stack.pop(-1)
        # 栈空
        if not stack:
            return True
        # 栈非空
        return False 