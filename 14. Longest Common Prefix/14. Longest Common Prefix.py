class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        for word in strs[1:]:
            while word.find(pref) != 0:
                pref = pref[:-1]
                if not pref:
                    return ""
        return pref

        