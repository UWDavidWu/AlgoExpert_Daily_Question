'''
Date: 2022/02/26
Author: David Wu
Link: https://www.algoexpert.io/questions/Group%20Anagrams

Question Summary:
return a list of anagram groups in no particular order

Optimal Complexity: O(w*n*log(n)) || O(wn)
'''

def groupAnagrams(words):
	result = {}
	sortedWords = ["".join(sorted(x)) for x in words]
	for idx,word in enumerate(sortedWords):
		if word not in result:
			result[word] = []
		result[word].append(idx)
		
	return [[words[y] for y in x] for x in result.values()]
		
