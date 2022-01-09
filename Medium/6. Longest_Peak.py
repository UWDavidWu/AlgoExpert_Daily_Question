'''
Date: 2022/01/09
Author: David Wu
Link: https://www.algoexpert.io/questions/Longest%20Peak

Question Summary:
return the longest peak of a given array

Example:
[1, 2, 3, 2, 1] => 5

Optimal Complexity: O(n) || O(1)
'''

def longestPeak(array):
    # Write your code here.
	longestPeakLength = 0
	i = 1
	while i < len(array)-1:
		isPeak = array[i-1] < array[i] and array[i] > array[i+1]
		if not isPeak:
			i += 1
			continue
			
		left = i -2
		while left >=0 and array[left] < array[left + 1]:
			left -= 1
		right = i+2
		while right < len(array) and array[right] < array[right - 1]:
			right +=1
		
		current = right - left - 1
		longestPeakLength = max(longestPeakLength, current)
		i = right
	return longestPeakLength


if __name__ == '__main__': 
	testArray1 = [1, 2, 3, 2, 1]
	testArray2 = [1, 2, 3, 1, 2, 3]
	print(longestPeak(testArray1) == 5)
	print(longestPeak(testArray2) == 4)


    
