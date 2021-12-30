'''
Date: 2021/12/30
Author: David Wu
Link: https://www.algoexpert.io/questions/First%20Non-Repeating%20Character

Question Summary:
Write a function that determines if you
can generate the document using the available characters

Example:
"abcdcaf" => 1

Optimal Complexity: O(n) || O(1)
'''

def firstNonRepeatingCharacter(string):

	result = {}

	for x in string:
		if x not in result:
			result[x] = 0
		result[x] += 1
		
	for index,x in enumerate(string):
		if result[x] == 1:
			return index
	return -1

    
if __name__ == '__main__': 
	print(firstNonRepeatingCharacter("abcdcaf") == 1)


    
