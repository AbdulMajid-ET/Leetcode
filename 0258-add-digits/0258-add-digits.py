class Solution(object):
    def addDigits(self, num):
        
        while num > 9:
            total = 0

            for n in str(num):
                total += int(n)
            
            num = total

        return num