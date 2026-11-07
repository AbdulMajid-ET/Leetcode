class Solution(object):
    def judgeCircle(self, moves):

        horizontal = 0
        vertical = 0

        for move in moves:
            
            if move == "L":
                horizontal -= 1
            elif move == "R":
                horizontal += 1
            elif move == "U":
                vertical += 1
            elif move == "D":
                vertical -= 1

        return horizontal == 0 and vertical == 0