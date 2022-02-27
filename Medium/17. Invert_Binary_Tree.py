'''
Date: 2022/02/27
Author: David Wu
Link: https://www.algoexpert.io/questions/Invert%20Binary%20Tree

Question Summary:
Invert Binary Tree

Optimal Complexity: O(n) || O(d)
'''

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
		
def invertBinaryTree(tree):
	if tree is None:
		return
	swap(tree)
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)
		
def swap(tree):
	tree.left, tree.right = tree.right, tree.left

