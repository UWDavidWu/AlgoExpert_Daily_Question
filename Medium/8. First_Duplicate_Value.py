'''
Date: 2022/01/11
Author: David Wu
Link: https://www.algoexpert.io/questions/First%20Duplicate%20Value

Question Summary:
return the first duplicate value else -1

Example:
[2, 1, 3, 2] => 2

Optimal Complexity: O(n) || O(1)
'''

def firstDuplicateValue(array):
    
	for val in array:
		absVal = abs(val)
		if array[absVal - 1] < 0:
			return absVal
		array[absVal -1] *= -1
	return -1



if __name__ == '__main__': 
	testArray1 = [2, 1, 3, 2] 
	print(firstDuplicateValue(testArray1) == 2)


    
