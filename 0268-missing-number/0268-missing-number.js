var missingNumber = function( nums ) {
    let n = nums.length
    let expectedSum = n * (n + 1) / 2

    let actualSum = 0

    // we uses for of loop for array
    for ( let num of nums ) {
        actualSum += num
    }

    return expectedSum - actualSum
}

missingNumber([3, 0, 1])