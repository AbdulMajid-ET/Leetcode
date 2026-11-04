class Solution:
    def countDigits(self, num):
        original = num
        count = 0

        for digit in str(num):
            digit = int(digit)

            if original % digit == 0: # this checks divisibility
                count += 1

        return count

# the question is to check that each digit of num is divisible by each digit of num i mean divide each digit by itself