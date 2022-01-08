'''
Date: 2022/01/07
Author: David Wu
Link: https://www.algoexpert.io/questions/Single%20Cycle%20Check

Question Summary:
Array value as jumps, check if an array forms a single cycle

Example:
[2, 3, 1, -4, -4, 2] => True

Optimal Complexity: O(n) || O(1)
'''

def hasSingleCycle(array):
    
	landedTimes, currIdx = 0, 0
	while landedTimes < len(array):
		if landedTimes > 0 and currIdx == 0:
			return False
		landedTimes += 1
		currIdx = helper(currIdx, array)
	return currIdx == 0



def helper(currIdx, array):

	jump = array[currIdx]
	nextIdx = (currIdx + jump) % len(array)
	return nextIdx if nextIdx >=0 else nextIdx + len(array)
    
if __name__ == '__main__': 
	testArray1 = [2, 3, 1, -4, -4, 2]
	testArray2 = [1, 3, 5]
	print(hasSingleCycle(testArray1) == True)
	print(hasSingleCycle(testArray2) == False)


    
