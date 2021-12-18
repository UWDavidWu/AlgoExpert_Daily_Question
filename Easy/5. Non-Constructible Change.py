'''
Date: 2021/12/18
Author: David Wu
Link: https://www.algoexpert.io/questions/Non-Constructible%20Change

Question Summary:
  Given an array of positive integers representing the values of coins in your
  possession, write a function that returns the minimum amount of change (the
  minimum sum of money) that you cannot create 

  

Example:
[1, 2, 5] => 4

Optimal Complexity: O(nlogn) || O(1)
'''

def nonConstructibleChange(coins):
    
    coins.sort()
    current = 0

    for coin in coins:
        if coin > current +1:
            return current + 1
        current += coin
    return current +1

if __name__ == '__main__': 
    print(nonConstructibleChange([1, 2, 5]) == 4)
    
