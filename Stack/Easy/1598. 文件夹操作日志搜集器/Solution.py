class Solution:
    def minOperations(self, logs: List[str]) -> int:
        hie = 0
        for log in logs:
            if log == "../":
                if hie != 0:
                    hie -= 1
            elif log != "./":
                hie += 1
        return hie