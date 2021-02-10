class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i = len(S) - 1
        j = len(T) - 1
        while i >= 0 or j >= 0:
            cnt = 0
            while i >= 0:
                if S[i] == "#":
                    cnt += 1
                    i -= 1
                else:
                    if cnt > 0:
                        cnt -= 1
                        i -= 1
                    else:
                        break
            
            cnt = 0
            while j >= 0:
                if T[j] == "#":
                    cnt += 1
                    j -= 1
                else:
                    if cnt > 0:
                        cnt -= 1
                        j -= 1
                    else:
                        break

            if (i >= 0) ^ (j >= 0):
                return False
            if i >= 0 and j >= 0 and S[i] != T[j]:
                return False

            i -= 1
            j -= 1

        return True