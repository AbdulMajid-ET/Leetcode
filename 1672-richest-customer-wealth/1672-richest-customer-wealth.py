class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0

        for each in accounts:
            total = 0

            for cal in each:
                # Add each bank balance to total
                total += cal

            # Compare total with max_wealth
            if total > max_wealth:
                max_wealth = total

        return max_wealth