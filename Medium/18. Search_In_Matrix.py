'''
Date: 2022/02/28
Author: David Wu
Link: https://www.algoexpert.io/questions/Search%20In%20Sorted%20Matrix

Question Summary:
return target position from a given martrix

Optimal Complexity: O(n + m) || O(1)
'''


def searchInSortedMatrix(matrix, target):
	currentRow = 0
	currentCol = len(matrix[0]) - 1
	
	while currentRow < len(matrix) and currentCol >=0:
		currentValue = matrix[currentRow][currentCol]
		if target > currentValue:
			currentRow += 1
		elif target < currentValue:
			currentCol -= 1
		else:
			return[currentRow, currentCol]
	return[-1,-1]

