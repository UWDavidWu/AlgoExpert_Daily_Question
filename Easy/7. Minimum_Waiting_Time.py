'''
Date: 2021/12/20
Author: David Wu
Link: https://www.algoexpert.io/questions/Minimum%20Waiting%20Time

Question Summary:
waiting time is defined as the amount of time that it must
wait before its execution starts. In other words, if a query is executed
second, then its waiting time is the duration of the first query; if a query
is executed third, then its waiting time is the sum of the durations of the
first two queries.

Example:
[3, 2, 1, 2, 6] => 17

Optimal Complexity: O(nlogn) || O(1)
'''

def minimumWaitingTime(queries):
	queries.sort(reverse=True)

	total = 0
	for index, duration in enumerate(queries):
		total += duration * index
		
	return total

if __name__ == '__main__': 
	testArray1 = [3, 2, 1, 2, 6]
	print(minimumWaitingTime(testArray1) == 17)
    




    
