'''
Date: 2022/02/25
Author: David Wu
Link: https://www.algoexpert.io/questions/Find%20Kth%20Largest%20Value%20In%20BST

Question Summary:
validate BST

Optimal Complexity: O(n) || O(n)
'''

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
	return inorder(tree,[])[-k]

def inorder(tree, array):
	if tree is not None:
		inorder(tree.left, array)
		array.append(tree.value)
		inorder(tree.right, array)
	return array

    
