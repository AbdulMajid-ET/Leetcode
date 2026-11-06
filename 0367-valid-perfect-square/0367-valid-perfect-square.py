class Solution(object):
    def isPerfectSquare( self, num ):
        # Start checking from 1 here (i = 1) 
        i = 1

        # Keep check to reach square becomes greater than num
        while i * i <= num:

            # this finds the perfect ok square!! otherwise the second return statement return false
            if i * i == num:
                return True

            i += 1
        return False