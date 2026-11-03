class Solution(object):
    def isSameAfterReversals(self, num):

        reverse = int(str(num)[::-1])
        double_reversal = int(str(reverse)[::-1])

        return num == double_reversal

