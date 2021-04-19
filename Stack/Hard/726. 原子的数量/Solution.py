class Solution:
    def countOfAtoms(self, formula: str) -> str:
        res = ""
        hash_ = self.recur(formula)
        for atom, num in sorted(hash_.items(), key=lambda x: x[0]):
            res += atom
            if num != 1:
                res += str(num)
        return res

    def add(self, res, atom, num):
        if not atom:
            pass
        elif type(atom) == str:
            res[atom] += num
        else:
            for k, v in atom.items():
                res[k] += v * num
        return res

    def recur(self, formula: str) -> str:
        from collections import defaultdict

        num = 1
        atom = ""
        res = defaultdict(int)

        i = 0
        while i < len(formula):
            if formula[i].isdigit():
                if num == 1 and not formula[i-1].isdigit():
                    num = int(formula[i])
                else:
                    num = num * 10 + int(formula[i])
            elif ord(formula[i]) >= ord("A") and ord(formula[i]) <= ord("Z"):
                res = self.add(res, atom, num)
                atom = formula[i]
                num = 1
            elif ord(formula[i]) >= ord("a") and ord(formula[i]) <= ord("z"):
                atom += formula[i]
            elif formula[i] == "(":
                res = self.add(res, atom, num)
                cnt = 1
                j = i+1
                while True:
                    if formula[j] == "(":
                        cnt += 1
                    elif formula[j] == ")":
                        cnt -= 1
                    if cnt == 0:
                        break
                    j += 1
                atom = self.recur(formula[i+1:j])
                num = 1
                i = j
            else:
                pass
            
            i += 1

        res = self.add(res, atom, num)

        return res