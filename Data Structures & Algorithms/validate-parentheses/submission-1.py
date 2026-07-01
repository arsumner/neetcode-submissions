class Solution:
    def isValid(self, s: str) -> bool:
        length = len(string) // 2
        end_index = len(string) - 1
        brackets = {

            '[': ']',
            '{': '}',
            '(': ')'

        }

        for i in range(length):
            if brackets[string[i]] != string[end_index]:
                return False
            else:
                end_index -= 1
        return True