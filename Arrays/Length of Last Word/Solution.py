class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        length = 0
        for char in s[::-1]:
            if char == " ":
                break
            length += 1
        return length
