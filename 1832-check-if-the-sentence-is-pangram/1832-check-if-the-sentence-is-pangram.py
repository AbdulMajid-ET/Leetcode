class Solution(object):
    def checkIfPangram(self, sentence):
        alpha = "abcdefghijklmnopqrstuvwxyz"

        for s in alpha:
            if s not in sentence:
                return False

        return True