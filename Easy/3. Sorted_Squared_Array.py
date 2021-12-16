'''
Date: 2021/12/16
Author: David Wu
Link: https://www.algoexpert.io/questions/Sorted%20Squared%20Array

Question Summary:
Square an ascending array 

Example:
[-3, -2, 1, 2, 5] => [1, 4, 4, 9, 25]
[1, 3, 5, 6, 7] => [1, 9, 25, 36, 49]

Optimal Complexity: O(n) || O(n)
'''

def sortedSquaredArray(array):

    result = [0] * len(array)
    small, large = 0, len(array) - 1

    for index in reversed(range(len(array))):
        smallVal, largeVal = array[small], array[large]
        
        if abs(smallVal) > abs(largeVal):
            result[index] = smallVal ** 2
            small += 1
        else:
            result[index] = largeVal ** 2
            large -= 1
            
    return result

if __name__ == '__main__':
    testArray1 = [-3, -2, 1, 2, 5]
    resultArray1 = [1, 4, 4, 9, 25]
    testArray2 = [1, 3, 5, 6, 7]
    resultArray2 = [1, 9, 25, 36, 49]
    
    print(sortedSquaredArray(testArray1) == resultArray1)
    print(sortedSquaredArray(testArray2) == resultArray2)
