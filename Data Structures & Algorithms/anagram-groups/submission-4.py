from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for i in range(len(s)):
                count[ord(s[i]) - ord("a")] += 1
            result[tuple(count)].append(s)

        return result


test = Solution()
test.groupAnagrams(["ate", "rat", "tea"])
