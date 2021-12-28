'''
Date: 2021/12/28
Author: David Wu
Link: https://www.algoexpert.io/questions/Run-Length%20Encoding

Question Summary:
Write a function that takes in a non-empty string and returns its run-length
encoding.

Example:
"AAABBC" => "3A2B1C"

Optimal Complexity: O(n) || O(n)
'''

def runLengthEncoding(string):
    
	result = ""
	counter = 1
	for i in range(1,len(string)):
		if string[i] != string[i-1] or counter == 9:
			result += f"{counter}{string[i-1]}"
			counter = 0
		counter +=1
	result += f"{counter}{string[-1]}"
	return result
    
if __name__ == '__main__': 
	print(runLengthEncoding("AAABBC") == "3A2B1C")


    
