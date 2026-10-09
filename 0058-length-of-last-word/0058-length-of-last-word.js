var lengthOfLastWord = function(s) {
    const words = s.trim().split(" ")
    return words[words.length-1].length
}

lengthOfLastWord("luffy is still joyboy")
// Orewa Luffyy