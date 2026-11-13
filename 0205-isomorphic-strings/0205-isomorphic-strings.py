
class Solution(object):
    def isIsomorphic(self, s, t):
        map_st = {}
        map_ts = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            # Check mapping from s to t
            if char_s in map_st:
                if map_st[char_s] != char_t:
                    return False
            else:
                map_st[char_s] = char_t

            # Check mapping from t to s
            if char_t in map_ts:
                if map_ts[char_t] != char_s:
                    return False
            else:
                map_ts[char_t] = char_s

        return True
