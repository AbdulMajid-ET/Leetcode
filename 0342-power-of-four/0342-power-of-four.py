class Solution(object):

  def isPowerOfFour(self, n):
    # Powers of four are always positive (1, 4, 16, 64, ...)
    if n <= 0:
      return False

    # Divide by 4 as long as n is divisible by 4
    while n % 4 == 0:
      n //= 4

    # If we reach 1, n was a power of four
    return n == 1