'''
Date: 2022/01/12
Author: David Wu
Link: https://www.algoexpert.io/questions/Merge%20Overlapping%20Intervals

Question Summary:
merge overlapping intervals

Example:
[[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]] => [[1, 2], [3, 8], [9, 10]]

Optimal Complexity: O(n) || O(1)
'''

def mergeOverlappingIntervals(intervals):
    
	sortedIntervals = sorted(intervals, key= lambda x: x[0])

	result = []
	current = sortedIntervals[0]
	result.append(current)

	for nextInterval in sortedIntervals:
		_, currentEnd = current
		nextStart, nextEnd = nextInterval
		
		if currentEnd >= nextStart:
			current[1] = max(currentEnd, nextEnd)
		else:
			current = nextInterval
			result.append(current)
	return result



if __name__ == '__main__': 
	testArray1 = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]] 
	resultArray1 = [[1, 2], [3, 8], [9, 10]]
	print(mergeOverlappingIntervals(testArray1) == resultArray1)


    
