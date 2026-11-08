class Solution( object ):
    def arrayStringsAreEqual( self, word1, word2 ):

        string1 = "".join( word1 ) # convert the word1 list into a string 
        string2 = "".join( word2 ) # convert the word2 list into a string 

        if string1 == string2: # then compare those string 
            return True # if it is true return True otherwise False
        
        return False