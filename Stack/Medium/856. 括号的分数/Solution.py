class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack_score = [0]
        stack_par = []
        for c in S:
            if c == "(":
                stack_par.append(c)
                stack_score.append(0)
            else:
                stack_par.pop()
                score_top = stack_score.pop()
                if score_top == 0:
                    stack_score[-1] += 1
                else:
                    stack_score[-1] += 2 * score_top
        return stack_score[0]