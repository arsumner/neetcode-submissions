class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        counts = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        for num, count in counts.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
            

test = Solution()
t = test.topKFrequent([1,2,2,3,3], 2)
