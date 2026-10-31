class Solution:
    def strStr( self, haystack, needle ):
        return haystack.find(needle)
        # find returns the index of the first occurrence of a substring when the substring is not found it 
        # returns -1

        # haystack = "sadbutsad"
        # needle = "sad"