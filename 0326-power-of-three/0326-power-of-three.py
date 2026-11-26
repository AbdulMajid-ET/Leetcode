class Solution(object):
  def isPowerOfThree(self, n):
    # Powers of three are always positive (1, 3, 9, 27, ...)
    if n <= 0:
      return False

    # Divide by 3 as long as n is divisible by 3
    while n % 3 == 0:
      n //= 3

    # If we end up with 1, every factor was a 3
    return n == 1