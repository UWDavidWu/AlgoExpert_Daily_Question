'''
Date: 2022/01/08
Author: David Wu
Link: https://www.algoexpert.io/questions/Binary%20Search

Question Summary:
Binary search

Example:
[1, 2, 3, 4], 2 => 1

Optimal Complexity: O(nlogn) || O(1)
'''

def binarySearch(array, target):
 
	left, right = 0, len(array) -1
	while left <= right:
		middle = (right + left)//2
		middleVal = array[middle]
		if  middleVal == target:
			return middle
		elif middleVal < target:
			left = middle + 1
		else:
			right = middle - 1
	return -1

    
if __name__ == '__main__': 
	print(binarySearch([1, 2, 3, 4], 2) == 1)


    
