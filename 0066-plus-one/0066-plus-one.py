class Solution:
    def plusOne(self, digits):

        for i in range(len(digits) - 1, -1, -1):
            # for i in range(2, -1, -1) this runs backwards

            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        digits.insert(0, 1)
        # where you want to add item here we use insert method to add a value at a specific index using 
        # insert(index, item)

        return digits