'''
Date: 2021/12/23
Author: David Wu
Link: https://www.algoexpert.io/questions/Nth%20Fibonacci

Question Summary:
Write a function that takes in an integerand returns the nth Fibonacci number

Example:
2 => 1
6 => 5

Optimal Complexity: O(n) || O(1)
'''

def getNthFib(n):
    
	lastTwo = [0, 1]
	counter = 3
	while counter <= n:
		nextFib = lastTwo[0] + lastTwo[1]
		lastTwo[0], lastTwo[1] = lastTwo[1], nextFib
		counter += 1
	return lastTwo[1] if n > 1 else lastTwo[0]

    
if __name__ == '__main__': 

	print(getNthFib(6) == 5)
	print(getNthFib(7) == 8)


    
