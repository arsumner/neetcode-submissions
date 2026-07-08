from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        res = defaultdict(list)

        for s in strs:
            charCount = [0] * 26
            for i in s:
                charCount[ord(i) - ord('a')] += 1
            charCount = tuple(charCount)
            res[charCount].append(s)

        answer = []
        for i in res.values():
            answer.append(i)

        return answer

test = Solution()
test.groupAnagrams(["ate", "rat", "tea"])
