class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans = ""  # Initialize an empty string to store the common prefix
        v = sorted(v)  # Sort the list of strings lexicographically

        first = v[0]  # The first string after sorting
        last = v[-1]  # The last string after sorting

        # Iterate through the characters of the first and last strings
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans  # If a mismatch is found, return the current common prefix
            ans += first[i]  # Append the character to the common prefix

        return ans  # Return the longest common prefix found
