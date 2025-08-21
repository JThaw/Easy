""" 
Given an integer x, return true if x is a palindrome, and false otherwise.
# Without converting to string 

Example 1 : 
    Input x = 121
    Output : true 
    Explanation : 121 reads as 121 from left toright and from right to left
    
Example 2: 
    Input  = -121
    Output : false
    Explanation : -121 >> reverse 121-. (not Palindrone)
    
Example 3 : 
    Input = 10
    Output : false 
    Explanation : 10 != 01 
"""
class Solution : 
    #using string 
    def isPalindrome_string(self, x):
        if x< 0 :
            return False
        return str(x) == str(x)[::-1]
    
    def isPalindrome_integer(self,x):
        if x < 0 : 
            return False
        org = x 
        rev = 0 
        while x>0 :
            rev = rev * 10 + x % 10
            x //=10
        return rev == org
    
solution = Solution()
print("##### INTEGER ####")
print(solution.isPalindrome_integer(121))
print(solution.isPalindrome_integer(-121))
print(solution.isPalindrome_integer(10))

print("##### String ####")
print(solution.isPalindrome_string(121))
print(solution.isPalindrome_string(-121))
print(solution.isPalindrome_string(10))
    