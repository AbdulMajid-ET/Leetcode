class Solution(object):
    def longestCommonPrefix(self, strs):

        if not strs:
            return ""

        result = ""

        for i in range(len(strs[0])):
            for word in strs:

                if i >= len(word) or word[i] != strs[0][i]:# Check if the current word is too short or not match
                    return result

            result += strs[0][i]

        return result