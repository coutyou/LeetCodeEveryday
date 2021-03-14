class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        for s in logs:
            temp = s.split(':')
            if temp[1] == 'start':
                stack.append(temp)
            else:
                time = int(temp[2]) - int(stack.pop()[2]) + 1
                res[int(temp[0])] += time
                if stack:
                    res[int(stack[-1][0])] -= time   
        return res