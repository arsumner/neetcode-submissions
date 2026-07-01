class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        freq = [[] for i in range(len(nums) + 1)]
        for n, c in counts.items():
            freq[c].append(n)

        answer = []   
        for i in range(len(freq) - 1, 0, -1):
           for n in freq[i]:
            res.append(n)
            if len(answer) == k:
                return answer
        return answer
