class Solution:
    def lengthOfLongestSubstring(self, s):

        seen = set()
        left = 0
        max_length = 0

        for right in range(len( s )):

            while s[right] in seen:
                seen.remove(s[ left ])
                left += 1

            seen.add(s[ right ])

            current_length = right - left + 1

            max_length = max( max_length, current_length )

        return max_length

'''
We use the Sliding Window technique with a set() to find the longest substring without repeating characters. We use two pointers, left and right, to maintain the substring window. The for loop moves through the string, while the while loop checks for duplicate characters. We use remove() to remove duplicates, add() to insert unique characters, max() to update the longest substring length, and len() to get the string length. Finally, we return max_length.
'''