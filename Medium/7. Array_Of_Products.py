'''
Date: 2022/01/10
Author: David Wu
Link: https://www.algoexpert.io/questions/Array%20Of%20Products

Question Summary:
return an array with product of every other number in array

Example:
[5, 1, 4, 2] => [8, 40, 10, 20]

Optimal Complexity: O(n) || O(1)
'''

def arrayOfProducts(array):

	result = [1] * len(array)

	left = 1
	for i in range(len(array)):
		result[i] = left
		left *= array[i]

	right = 1
	for i in reversed(range(len(array))):
		result[i] *= right
		right *= array[i]
	
	return result



if __name__ == '__main__': 
	testArray1 = [5, 1, 4, 2]
	resultArray1 = [8, 40, 10, 20]
	print(arrayOfProducts(testArray1) == resultArray1)


    
