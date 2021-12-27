'''
Date: 2021/12/27
Author: David Wu
Link: https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor

Question Summary:
Given a non-empty string of lowercase letters and a non-negative integer
representing a key, write a function that returns a new string obtained by
shifting every letter in the input string by k positions in the alphabet,
where k is the key.

Example:
"xyz", 2 => "zab"

Optimal Complexity: O(n) || O(n)
'''

def caesarCipherEncryptor(string, key):
    
	mapping = list("abcdefghijklmnopqrstuvwxyz")
	result = ""

	for index,x in enumerate(string):
		result+=mapping[(mapping.index(string[index]) + key)% 26]
	return result
    
if __name__ == '__main__': 
	print(caesarCipherEncryptor("xyz", 2 ) == "zab")


    
