class Solution:

    def encode(self, strs: list[str]) -> str:
        result = ""
        for s in strs:
            result +=  str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> list[str]:
        result = []
        i, j = 0, 1
        while j < len(s):
            if s[j] != "#":
                j += 1
                i += 1
            else:
                length = s[i]
                result.append(s[j + 1: j + 1 + int(length)])
                i = j + 1 + int(length)
                j = i + 1
        print(result)
        return result

