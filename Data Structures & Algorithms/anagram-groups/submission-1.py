class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        for s in strs:
            letter_count = 26 * [0]
            for c in s:
                letter_count[ord(c) - 97] += 1
            print(letters_count)

            if letter_count not in strs_dict:
                letter_count = strs_dict[[s]]
            else:
                strs_dict[s].append(s)
        return strs_dict.keys()
