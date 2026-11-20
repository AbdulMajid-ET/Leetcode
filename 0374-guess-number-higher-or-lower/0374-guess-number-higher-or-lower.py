
class Solution(object):
    def guessNumber(self, n):
        
        left = 1
        right = n

        while left <= right:
            
            mid = (left + right) // 2

            result = guess(mid)

            if result == 0:
                return mid

            elif result == -1:
                right = mid - 1

            else:
                left = mid + 1


# guess() is a predefined function provided by LeetCode.
'''
guess(num) == -1	Your guess is too high.
guess(num) == 1	Your guess is too low.
guess(num) == 0	Your guess is correct.
'''