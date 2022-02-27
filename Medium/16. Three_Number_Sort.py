'''
Date: 2022/02/27
Author: David Wu
Link: https://www.algoexpert.io/questions/Three%20Number%20Sort

Question Summary:
Sort the array accordinig to the order
requirement: mutate input array

Example:
[1, 0, 0, -1,-1, 0, 1, 1], [0, 1, -1] => [0, 0, 0, 1, 1, 1, -1, -1]

Optimal Complexity: O(n) || O(1)
'''

def threeNumberSort(array, order):

	count = [0,0,0]
	
	for ele in array:
		count[order.index(ele)] +=1
		
	for i in range(3):
		thisorder = order[i]
		thiscount = count[i]
		elementsBefore = sum(count[:i])
		for x in range(thiscount):
			currentIdx = elementsBefore + x
			array[currentIdx] = thisorder
		
	return array


if __name__ == '__main__': 
	testArray1 = [1, 0, 0, -1,-1, 0, 1, 1]
	testArray2 = [0, 1, -1]
	resultArray = [0, 0, 0, 1, 1, 1, -1, -1]
	print(threeNumberSort(testArray1, testArray2) == resultArray)