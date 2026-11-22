class Solution(object):
    def groupAnagrams(self, strs):

        groups = {}

        for word in strs:

            # Sort the characters of the word
            key = "".join(sorted(word))

            # Check if the key already exists
            if key not in groups:
                groups[key] = []

            # Add the original word to the group
            groups[key].append(word)

        return list(groups.values())

    