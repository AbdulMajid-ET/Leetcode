var kidsWithCandies = function(candies, extraCandies) {
    let result = []
    let greatest = 0
    for ( let i = 0; i < candies.length; i++ ) {
        if ( candies[i] > greatest ) {
            greatest = candies[i]
        }
    }
    for ( let i = 0; i < candies.length; i++ ) {
        if ( candies[i] + extraCandies >= greatest ) {
            result.push(true)
        } else {
            result.push(false)
        }
    }
    return result
};

kidsWithCandies([2, 3, 5, 1, 3], 3)