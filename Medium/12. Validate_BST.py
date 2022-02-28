'''
Date: 2022/02/25
Author: David Wu
Link: https://www.algoexpert.io/questions/Validate%20BST

Question Summary:
validate BST

Optimal Complexity: O(n) || O(n)
'''

def validateBst(tree):
    return helper(tree,float("-inf"),float("inf"))

def helper(tree, minVal, maxVal):
	if tree is None:
		return True
	if tree.value < minVal or tree.value >= maxVal:
		return False
	return helper(tree.left, minVal, tree.value) and helper(tree.right, tree.value, maxVal)


    
