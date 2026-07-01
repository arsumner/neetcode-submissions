class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        for s in strs:
            letter_count = 26 * [0]
            for c in s:
                print(ord(c))
                letter_count[ord(c) - 97] += 1
            if letter_count not in strs_dict:
                strs_dict[[s]] = letters_count
            else:
                strs_dict[s].append(s)
        return strs_dict.keys()
