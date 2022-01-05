'''
Date: 2022/01/05
Author: David Wu
Link: https://www.algoexpert.io/questions/Move%20Element%20To%20End

Question Summary:
Write a function that moves all instances of that integer in the 
array to the end of the array and returns the array

Example:
[2, 1, 2, 2, 2, 3, 4, 2], 2 => [1, 3, 4, 2, 2, 2, 2]

Optimal Complexity: O(n) || O(1)
'''

def moveElementToEnd(array, toMove):
	
	left,right = 0, len(array)-1
	
	while left < right:
		if array[left] == toMove and array[right] != toMove:
			array[left], array[right] = array[right], array[left]
			left +=1
			right -=1
		elif array[left] != toMove:
			left +=1
		elif array[right] == toMove:
			right -=1
	return array
    
if __name__ == '__main__': 
	testArray1 = [2, 1, 2, 2, 2, 3, 4, 2]
	resultArray2 = [4, 1, 3, 2, 2, 2, 2, 2]
	print(moveElementToEnd(testArray1, 2) == resultArray2)


    
