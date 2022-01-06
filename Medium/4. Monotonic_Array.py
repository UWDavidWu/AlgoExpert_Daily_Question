'''
Date: 2022/01/06
Author: David Wu
Link: https://www.algoexpert.io/questions/Monotonic%20Array

Question Summary:
check if an array is monodecreasing or monoincreasing

Example:
[1, 1, 3, 5, 7, 7, 9] => True

Optimal Complexity: O(n) || O(1)
'''

def isMonotonic(array):

	isincre,isdecre = True, True

	for i in range(1, len(array)):
		if array[i] > array[i-1]:
			isdecre = False
		elif array[i] < array[i-1]:
			isincre = False
	return isincre or isdecre
    
if __name__ == '__main__': 
	testArray1 = [1, 1, 3, 5, 7, 7, 9]
	testArray2 = [1, 3, 5, 3, 7, 9]
	print(isMonotonic(testArray1) == True)
	print(isMonotonic(testArray2) == False)


    
