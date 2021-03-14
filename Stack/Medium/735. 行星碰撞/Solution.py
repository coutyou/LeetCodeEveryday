class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            if not stack:
                stack.append(num)
            else:
                if num > 0:
                    stack.append(num)
                else:
                    while True:
                        if not stack or stack[-1] < 0:
                            stack.append(num)
                            break
                        else:
                            top = stack[-1]
                            if top == -num:
                                stack.pop()
                                break
                            elif top > -num:
                                break
                            else:
                                stack.pop()
        return stack
