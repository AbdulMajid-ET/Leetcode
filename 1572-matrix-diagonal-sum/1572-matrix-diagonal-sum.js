var diagonalSum = function(mat) {
    let sum = 0
    for( let i = 0; i < mat.length; i++ ) {
        sum = sum + mat[i][i]
        sum = sum + mat[i][mat.length - 1 - i]
    }

    if ( mat.length % 2 !== 0 ) {
        sum = sum - mat[Math.floor(mat.length / 2)][Math.floor(mat.length / 2)];
    }

    return sum;
};

diagonalSum([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])