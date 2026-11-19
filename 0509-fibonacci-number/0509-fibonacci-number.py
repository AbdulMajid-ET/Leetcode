
class Solution(object):
    def fib(self, n):

        # Handle the first two Fibonacci numbers
        if n == 0: 
            return 0

        if n == 1:
            return 1

        a = 0
        b = 1

        for i in range(2, n + 1):

            c = a + b

            # Update the previous numbers
            a = b
            b = c

        return b
