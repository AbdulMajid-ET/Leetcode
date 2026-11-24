class Solution(object):
  def isPowerOfTwo(self, n):
    if n <= 0:
      return False

    # Divide by 2 as long as n is even
    while n % 2 == 0:
      n //= 2

    # If we end up with 1, every factor was a 2
    return n == 1