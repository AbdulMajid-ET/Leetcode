class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False

        dict1 = {} # Character -> Word
        dict2 = {} # Word -> Character

        for char, word in zip(pattern, words):

            # Check if the character is already mappeddd
            # to a different word
            if char in dict1 and dict1[char] != word:
                return False

            # Check if the word is already mapped to a different character
            if word in dict2 and dict2[word] != char:
                return False

            # these to for storing the char to word and word to char mapping, finally 
            dict1[char] = word
            dict2[word] = char

        return True