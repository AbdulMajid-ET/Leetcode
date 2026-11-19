class Solution:
    def detectCapitalUse(self, word):

        if word.isupper():
            return True

        if word.islower():
            return True

        if word[0].isupper() and word[1:].islower():
            return True

        # If none of the conditions match, return False
        return False

'''
isupper() and islower() are built-in Python string methods used to check the capitalization of a string. The isupper() method checks whether all alphabetic characters are uppercase, while islower() checks whether all alphabetic characters are lowercase.
'''