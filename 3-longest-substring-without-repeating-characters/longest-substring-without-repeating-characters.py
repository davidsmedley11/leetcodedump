class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters_used = []
        substrings_used = []
        current_string = ""
        current_highest = 0
 
        for char in s:
            letters_used.append(char)
        
        for i in range(len(s)):
            current_string = ""
            for j in range(i, len(s)):
                if s[j] not in current_string:
                    current_string += s[j]
                else:
                    break
            substrings_used.append(current_string)

        for substrings in substrings_used:
            if len(substrings) > current_highest:
                current_highest = len(substrings)


        return current_highest



        
            