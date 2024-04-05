"""
3. Longest Substring Without Repeating Characters

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        count = 0
        max_val = 0
        for i in range(len(s)):
            if s[i] in h:
                x = h[s[i]]
                # h.pop(s[i])
                h = {}
                h[s[i]] = i
                if count > max_val:
                    max_val = count
                count = i - x 
            else:
                h[s[i]] = i
                count += 1
        if count > max_val:
            return count
        return max_val
if __name__ == "__main__":
    x = Solution()
    y = x.lengthOfLongestSubstring("abba")
    print(y)
