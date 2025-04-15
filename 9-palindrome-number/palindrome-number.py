class Solution:
    def isPalindrome(self, x: int) -> bool:

        x = str(x)

        def findPalindrome(left: int, right:int) -> str:
            while left >= 0 and right < len(x) and x[right] == x[left]:
                left -= 1
                right += 1
            return x[left + 1:right]

        longest_palindrome = ""
    
        for i in range(len(x)):

            current_palindrome = findPalindrome(i, i)
            if len(current_palindrome) > len(longest_palindrome):
                longest_palindrome = current_palindrome

            current_palindrome = findPalindrome(i, i + 1)
            if len(current_palindrome) > len(longest_palindrome):
                longest_palindrome = current_palindrome
        
        if x == longest_palindrome:
            return True
        else:
            return False
