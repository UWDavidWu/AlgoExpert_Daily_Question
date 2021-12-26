'''
Date: 2021/12/25
Author: David Wu
Link: https://www.algoexpert.io/questions/Find%20Three%20Largest%20Numbers

Question Summary:
Write a function that takes in an array of at least three integers and,
without sorting the input array, returns a sorted array of the three largest
integers in the input array.

Example:
[1, 2, 3, 5, 6] => [3, 5, 6]

Optimal Complexity: O(n) || O(1)
'''

def findThreeLargestNumbers(array):

	largestThree =  [float('-inf'),float('-inf'),float('-inf')]

	for val in array:
		if val > largestThree[-1]:
			shift(largestThree, val, 2)
		elif val > largestThree[-2]:
			shift(largestThree, val, 1)
		elif val > largestThree[-3]:
			shift(largestThree, val, 0)
	return largestThree
			
			
			
def shift(array, num, index):
	for x in range(index):
		array[x]= array[x+1]
	array[index] = num

    
if __name__ == '__main__': 
	print(findThreeLargestNumbers([1, 2, 3, 5, 6]) == [3, 5, 6])


    
