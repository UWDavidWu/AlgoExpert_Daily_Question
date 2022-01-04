'''
Date: 2022/01/04
Author: David Wu
Link: https://www.algoexpert.io/questions/Smallest%20Difference

Question Summary:
Find a pair from two array whose absolute difference is the smallest

Example:
[-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17] => [28,26]

Optimal Complexity: O(nlogn + mlogm) || O(1)
'''

def smallestDifference(arrayOne, arrayTwo):

	arrayOne.sort()
	arrayTwo.sort()

	pointer1, pointer2 = 0, 0
	small, small_pair = float("inf"), []


	while pointer1 < len(arrayOne) and pointer2 < len(arrayTwo):
		num1, num2 = arrayOne[pointer1], arrayTwo[pointer2]
		if num1 > num2:
			diff = num1 - num2
			pointer2 +=1
		elif num1 < num2:
			diff = num2 - num1
			pointer1 +=1
		else:
			return [num1, num2]
		if diff < small:
			small = diff
			small_pair =[num1, num2] 
	return small_pair
    
if __name__ == '__main__': 
	testArray1 = [-1, 5, 10, 20, 28, 3]
	testArray2 = [26, 134, 135, 15, 17]
	print(smallestDifference(testArray1, testArray2) == [28, 26])


    
