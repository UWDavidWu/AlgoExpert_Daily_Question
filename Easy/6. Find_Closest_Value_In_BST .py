'''
Date: 2021/12/19
Author: David Wu
Link: https://www.algoexpert.io/questions/Find%20Closest%20Value%20In%20BST

Question Summary:
Write a function that takes in a Binary Search Tree (BST) and a target integer
value and returns the closest value to that target value contained in the BST.

Example:
N/A

Optimal Complexity: O(n) || O(1)
'''

def findClosestValueInBst(tree, target):
    return helper(tree, target, tree.value)

def helper(tree, target, current):
	currentNode = tree
	while currentNode is not None:
		if abs(target - current) > abs(target - currentNode.value):
			current = currentNode.value
		if target < currentNode.value:
			currentNode = currentNode.left
		elif target > currentNode.value:
			currentNode = currentNode.right
		else:
			break
	return current


    
