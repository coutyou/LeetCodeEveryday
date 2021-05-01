class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        num2freq = defaultdict(int)
        freq2num = defaultdict(list)
        max_freq = 0
        for num in nums:
            num2freq[num] += 1
            max_freq = max(max_freq, num2freq[num])
        for num in num2freq:
            freq2num[num2freq[num]].append(num)
        res = []
        while len(res) < k:
            for num in freq2num[max_freq]:
                res.append(num)
            max_freq -= 1
        return res