'''
Date: 2021/12/21
Author: David Wu
Link: https://www.algoexpert.io/questions/Class%20Photos

Question Summary:
pass

Example:
pass

Optimal Complexity: O(nlogn) || O(1)
'''

def classPhotos(redShirtHeights, blueShirtHeights):

	redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)
	tallest = "red" if redShirtHeights[-1] > blueShirtHeights[-1] else "blue"
	
	for x in range(len(redShirtHeights)):
		redShirtHeight = redShirtHeights[x]
		blueShirtHeight = blueShirtHeights[x]
		
		if tallest == "red":
			if redShirtHeight <= blueShirtHeight:
				return False
		else:
			if redShirtHeight >= blueShirtHeight:
				return False
	return True

    




    
