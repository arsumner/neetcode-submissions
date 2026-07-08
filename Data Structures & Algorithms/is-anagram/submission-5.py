class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0] * 26
        
        for i in s:
            counts[ord(i) - ord("a")] += 1
        
        for i in t:
            counts[ord(i) - ord("a")] -= 1
        
        for i in range(len(counts)):
            if counts[i] != 0:
                return False
        
        return True
