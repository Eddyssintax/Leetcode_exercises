class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            "I": 1,

            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000

        }
        ans = 0

        for x in range(len(s)):
            if x < len(s) - 1 and nums[s[x]] < nums[s[x + 1]]:
                ans -= nums[s[x]]
            else:
                ans += nums[s[x]]
        return ans


n = Solution().romanToInt("MM4LCILX")

print(n)
