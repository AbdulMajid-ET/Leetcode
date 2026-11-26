class Solution(object):
  def isPalindrome(self, head):
    vals = []
    current = head

    # Collect all node values into a list
    while current:
      vals.append(current.val)
      current = current.next

    # Compare list with its reversed version
    return vals == vals[::-1]