class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        for i in nums:
            counts[i] = 1 + counts.get(i, 0)

        freq = [[] for i in range(len(nums) + 1)]
        for num, count in counts.items():
            freq[count].append(num)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
                for n in freq[i]:
                    result.append(n)
                    if len(result) == k:
                        return result

