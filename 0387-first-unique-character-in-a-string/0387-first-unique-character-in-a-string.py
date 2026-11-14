class Solution(object):
    def firstUniqChar(self, s):
        freq = {}

        for ss in s:
            if ss in freq:
                freq[ss] += 1
            else:
                freq[ss] = 1

        for index, char in enumerate(s):
            if freq[char] == 1:
                return index

        return -1