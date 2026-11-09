class Solution(object):
    def isPalindrome(self, s):

        clean = ""

        # Remove spaces and special characters
        # Convert all letters to lowercase
        for char in s:
            if char.isalnum(): # checks whether the character is a letter or number.
                clean += char.lower()

        # Reverse the cleaned string
        reverse = clean[::-1]

        if clean == reverse:
            return True
        else:
            return False