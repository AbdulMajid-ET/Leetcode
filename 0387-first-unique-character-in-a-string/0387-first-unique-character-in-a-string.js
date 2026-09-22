var firstUniqChar = function(s) {
    let count = {}

    // Count each character
    for ( let char of s ) {
        count[char] = (count[char] || 0) + 1
    }

    // Find the first character with count 1
    for ( let i = 0; i < s.length; i++ ) {
        if ( count[s[i]] === 1 ) {
            return i
        }
    }

    return -1
}

// firstUniqChar("leetcode")