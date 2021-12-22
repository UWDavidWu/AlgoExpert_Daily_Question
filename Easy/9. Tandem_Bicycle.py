'''
Date: 2021/12/21
Author: David Wu
Link: https://www.algoexpert.io/questions/Tandem%20Bicycle

Question Summary:
pass

Example:
pass

Optimal Complexity: O(nlogn) || O(1)
'''

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):

	redShirtSpeeds.sort()
	blueShirtSpeeds.sort()
	reverse_red = sorted(redShirtSpeeds, reverse=True)

	result = 0
	
	for x in range(len(redShirtSpeeds)):
		redShirtSpeed_rev = reverse_red[x]
		redShirtSpeed = redShirtSpeeds[x]
		blueShirtSpeed = blueShirtSpeeds[x]
		if not fastest:
			result += max(redShirtSpeed,blueShirtSpeed)
		else:
			result += max(redShirtSpeed_rev,blueShirtSpeed)	
	return result 

    




    
