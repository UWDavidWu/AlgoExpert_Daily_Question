'''
Date: 2022/01/03
Author: David Wu
Link: https://www.algoexpert.io/questions/Three%20Number%20Sum

Question Summary:
Three Numbers Sum

Example:
[12, 3, 1, 2, -6, 5, -8, 6], 0 => [[-8, 2, 6],[-8, 3, 5],[-6, 1, 5]]

Optimal Complexity: O(n^2) || O(n)
'''

def threeNumberSum(array, targetSum):

	result = []
	array.sort()
	
	
	for index,x in enumerate(array):
		left = index + 1
		right = len(array) - 1
		while left < right:
			threeSum = array[left] + array[right] + array[index]
			if threeSum == targetSum:
				result.append([array[index],array[left], array[right]])
				left +=1
				right -=1
			elif threeSum < targetSum:
				left +=1
			elif threeSum > targetSum:
				right -=1
	return result
    
if __name__ == '__main__': 
	testArray1 = [12, 3, 1, 2, -6, 5, -8, 6]
	resultArray1 = [[-8, 2, 6],[-8, 3, 5],[-6, 1, 5]]
	print(threeNumberSum(testArray1,0) == resultArray1)


    
