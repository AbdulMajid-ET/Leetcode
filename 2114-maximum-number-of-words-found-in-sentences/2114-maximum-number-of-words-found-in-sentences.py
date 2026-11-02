class Solution(object):
    def mostWordsFound( self, sentences ):
        max_count = 0

        for sentence in sentences:
            if (sentence.count(" ") + 1) > max_count:
                max_count = sentence.count(" ") + 1

        return max_count
'''
Here i use count for counting the spaces between the words in addition with 1 increment cuz of 
each sentences count is one plus higher than the spaces so that's why i use + 1 after the count built
in function
'''