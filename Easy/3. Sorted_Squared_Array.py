'''
Date: 2021/12/16
Author: David Wu
Link: https://www.algoexpert.io/questions/Sorted%20Squared%20Array

Question Summary:
Determine where sequence is a subsequence of an array

Example:
[1, 2, 3, 4, 5], [1, 3, 5] => True
[1, 2, 3, 4, 5], [1, 5, 6] => False

Optimal Complexity: O(n) || O(1)
'''

def isValidSubsequence(array, sequence):

    Index = 0
    for val in array:
        if val == sequence[Index]:
            Index += 1    
        if Index == len(sequence):
            return True
    return False

if __name__ == '__main__':
    testArray1 = [11, 3, -1, 9, 12]
    testArray2 = [11, -1, 12]
    
    print(isValidSubsequence(testArray1, testArray2)==True)
