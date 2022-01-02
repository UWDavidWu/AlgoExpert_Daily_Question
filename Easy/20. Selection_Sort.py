'''
Date: 2022/01/02
Author: David Wu
Link: https://www.algoexpert.io/questions/Selection%20Sort

Question Summary:
Selection Sort

Example:
[1,3,2,5] => [1,2,3,5]

Optimal Complexity: O(n^2) || O(1)
'''

def selectionSort(array):

	currentIdx = 0

	while currentIdx < len(array):
		smallIdx = currentIdx
		for i in range(currentIdx +1, len(array)):
			if array[i] < array[smallIdx]:
				smallIdx = i 
		array[currentIdx], array[smallIdx] = array[smallIdx], array[currentIdx]
		currentIdx+=1	
	return array

    
if __name__ == '__main__': 
	print(selectionSort([1,3,2,5]) == [1,2,3,5])


    
