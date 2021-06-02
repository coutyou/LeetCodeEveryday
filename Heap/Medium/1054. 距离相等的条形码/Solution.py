class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        map_ = {}
        max_code = 0
        max_freq = 0
        n = len(barcodes)
        for code in barcodes:
            if code not in map_:
                map_[code] = 1
            else:
                map_[code] += 1
            if map_[code] > max_freq:
                max_freq = map_[code]
                max_code = code
        del map_[max_code]
        
        idx = 0
        res = [0 for _ in range(n)]
        for _ in range(max_freq):
            res[idx] = max_code
            idx += 2
            
        if idx >= n:
            idx = 1
        
        for code,freq in map_.items():
            for _ in range(freq):
                res[idx] = code
                idx += 2
                if idx >= n:
                    idx = 1

        return res

