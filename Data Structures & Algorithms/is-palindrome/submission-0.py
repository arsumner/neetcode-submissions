class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ("".join([char for char in s if char.isalpha()])).lower()
        print(stripped)
        

        r = len(stripped) - 1
        for i in range(len(stripped)//2):
            if stripped[i] != stripped[r]:
                return False
            r -=1
        return True

test = Solution()
test.isPalindrome("Was it a car or a cat I saw?")