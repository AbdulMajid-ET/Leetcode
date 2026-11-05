class Solution(object):
    def reverseWords(self, s):
        word = s.split()

        reversed_words = word[::-1] #short way of reversing of slicing
        result = " ".join(reversed_words)
        return result