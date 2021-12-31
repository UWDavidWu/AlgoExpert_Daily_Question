'''
Date: 2021/12/31
Author: David Wu
Link: https://www.algoexpert.io/questions/Bubble%20Sort

Question Summary:
Bubble Sort

Example:
[1,3,2,5] => [1,2,3,5]

Optimal Complexity: O(n^2) || O(1)
'''

def bubbleSort(array):
    
	isSorted, counter = False, 0
	
	while not isSorted:
		isSorted = True
		for i in range(len(array)-1-counter):
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
				isSorted = False
		counter +=1
	return array

    
if __name__ == '__main__': 
	print(bubbleSort([1,3,2,5]) == [1,2,3,5])


    
