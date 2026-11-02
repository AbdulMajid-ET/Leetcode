class Solution(object):
    def subtractProductAndSum( self, n ):
        product = 1
        total = 0

        for i in str(n): # first change the input to string to loop through n
            i = int(i) # then convert it to integer to calculate the Product of digit and Sum of digit

            product = product * i
            total = total + i

        return product - total

# n = 234