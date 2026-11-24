class Solution(object):
  def duplicateZeros(self, arr):
    temp = []

    # Build a new list while duplicating every 0
    for num in arr:
      temp.append(num)
      if num == 0:
        temp.append(0)

    # Copy the first len(arr) elements back into arr in place
    for i in range(len(arr)):
      arr[i] = temp[i]