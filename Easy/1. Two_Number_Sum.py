'''
Date: 2021/12/14
Author: David Wu
Link: https://www.algoexpert.io/questions/Two%20Number%20Sum

Question Summary:
Find pairs in the array that sums to target

Example:
[1, 2, 3], 5 => [2, 3]

Optimal Complexity: O(nlog(n)) || O(1)
'''

def twoNumberSum(array, target):
    
    array.sort()
    left,right = 0, len(array) - 1
	
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == target:
            return [array[left], array[right]]
        elif currentSum < target:
            left += 1
        elif currentSum > target:
            right -= 1
    return []


if __name__ == '__main__':
    testArray1 = [1, 3, 6, 9, -1]
    resultArray1 = [-1, 1]
    print(twoNumberSum(testArray1, 0)==resultArray1)
