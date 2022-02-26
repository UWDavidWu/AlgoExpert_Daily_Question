'''
Date: 2022/02/26
Author: David Wu
Link: https://www.algoexpert.io/questions/Breadth-first%20Search

Question Summary:
BFS

Optimal Complexity: O(V + E) || O(V)
'''

class Node:
	def __init__(self, name):
		self.children = []
		self.name = name

	def addChild(self, name):
		self.children.append(Node(name))
		return self

	def breadthFirstSearch(self, array):
		queue = [self]
		while len(queue) > 0:
			current = queue.pop(0)
			array.append(current.name)
			for child in current.children:
				queue.append(child)
		return array
		
