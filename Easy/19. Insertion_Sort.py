'''
Date: 2022/01/01
Author: David Wu
Link: https://www.algoexpert.io/questions/Insertion%20Sort

Question Summary:
Insertion Sort

Example:
[1,3,2,5] => [1,2,3,5]

Optimal Complexity: O(n^2) || O(1)
'''

def insertionSort(array):
    
	for i in range(1, len(array)):
		j = i 
		while j > 0 and array[j]< array[j-1]:
			array[j], array[j-1] = array[j-1], array[j]
			j -=1
	return array

    
if __name__ == '__main__': 
	print(insertionSort([1,3,2,5]) == [1,2,3,5])


    
