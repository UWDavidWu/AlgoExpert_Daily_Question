'''
Date: 2021/12/26
Author: David Wu
Link: https://www.algoexpert.io/questions/Palindrome%20Check

Question Summary:
determine if a string is palindrome or not

Example:
"abcdcba" => True

Optimal Complexity: O(n) || O(1)
'''

def isPalindrome(string):
	left, right = 0, len(string) -1

	while left < right:
		if string[left] != string[right]:
			return False
		left += 1
		right -= 1					
	return True

'''
def isPalindrome(string):
    return string == string[::-1]
'''
    
if __name__ == '__main__': 
	print(isPalindrome("abcdcba") == True)


    
