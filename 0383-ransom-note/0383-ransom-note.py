class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        freq = {}

        for m in magazine:
            if m in freq:
                freq[m] = freq[m] + 1
            else:
                freq[m] = 1

        for r in ransomNote:
            if r in freq and freq[r] > 0:
                freq[r] = freq[r] - 1
            else:
                return False

        return True