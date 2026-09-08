var moveZeroes = function( nums ) {
    let result = []

    for ( let i = 0; i < nums.length; i++ ) {
        if ( nums[i] !== 0 ) {
          result.push(nums[i])  
        }
    }

    while ( result.length < nums.length ) {
        result.push(0)
    }

    for ( let i = 0; i < nums.length; i++ ) {
        nums[i] = result[i]
    }
}

moveZeroes([0, 1, 0, 3, 12])
// Zeroesss