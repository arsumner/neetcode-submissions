class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = freq.get(i, 0)
            freq[i] += 1
        for i in range(0, len(nums) - k):
            freq.pop(min(freq.values()))
        return freq.keys()
            