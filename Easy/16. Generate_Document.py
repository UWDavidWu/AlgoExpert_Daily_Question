'''
Date: 2021/12/29
Author: David Wu
Link: https://www.algoexpert.io/questions/Generate%20Document

Question Summary:
Write a function that determines if you
can generate the document using the available characters

Example:
"this is good", "goothi iss d" => True

Optimal Complexity: O(n+m) || O(c)
'''

def generateDocument(characters, document):
    
	chartersWeHave = {}
	
	for char in characters:
		if char not in chartersWeHave:
			chartersWeHave[char] = 0
		chartersWeHave[char] += 1
		
	for char in document:
		if char not in chartersWeHave or chartersWeHave[char] == 0:
			return False
		chartersWeHave[char] -= 1
	return True

    
if __name__ == '__main__': 
	print(generateDocument("this is good", "goothi iss d") == True)


    
