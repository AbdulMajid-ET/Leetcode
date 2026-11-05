class Solution(object):
    def reverseWords(self, s):
        result = s.split(" ")
        new_list = []
        new = ""

        for res in result:
            new_list.append(res[::-1])
            new = " ".join(new_list)
        return new