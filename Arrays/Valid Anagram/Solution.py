from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_dict_s = defaultdict(int)
        chars_dict_t = defaultdict(int)
        if len(s) != len(t):
            return False

        for idx in range(len(s)):
            chars_dict_s[s[idx]] += 1
            chars_dict_t[t[idx]] += 1

        if len(chars_dict_s) != len(chars_dict_t):
            return False

        for key in chars_dict_s:
            if chars_dict_s[key] != chars_dict_t[key]:
                return False
        return True
