'''
Date: 2021/12/24
Author: David Wu
Link: https://www.algoexpert.io/questions/Product%20Sum

Question Summary:
The product sum of [x, [y, [z]]] is x + 2 * (y + 3z)

Example:
[1, [2, [3]]] = 1 + 2 * (2 + 3 * 3) = 23

Optimal Complexity: O(n) || O(c)
'''

def productSum(array, currentLevel=1):
	currentSum = 0
	for x in array:
		if type(x) == list:
			currentSum += productSum(x, currentLevel+1)
		else:
			currentSum += x
			
	return currentSum * currentLevel

    
if __name__ == '__main__': 

	print(productSum([1, [2, [3]]]) == 23)


    
