var majorityElement = function(nums) {
    let count = {}

    for (let num of nums) {
        count[num] = (count[num] || 0) + 1
        // If the number doesn't exist yet, start counting from 0

        if (count[num] > nums.length / 2) {
        // Check if the current number appears more than half of the array
            return num
        }
    }
}

majorityElement([2,2,1,1,1,2,2])