class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = freq.get(i, 0)
            freq[i] += 1
        for i in range(0, len(freq) - k):
            freq.pop(min(freq.values()))
        return freq.keys()