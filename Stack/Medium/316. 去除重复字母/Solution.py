class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        in_stack = set()
        remain = collections.Counter(s)

        for c in s:
            if c not in in_stack:
                while stack and c < stack[-1] and remain[stack[-1]] > 0:
                    in_stack.remove(stack.pop())
                stack.append(c)
                in_stack.add(c)
            remain[c] -= 1

        return "".join(stack)