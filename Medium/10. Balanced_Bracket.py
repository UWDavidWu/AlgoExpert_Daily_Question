'''
Date: 2022/02/22
Author: David Wu
Link: https://www.algoexpert.io/questions/Balanced%20Brackets

Question Summary:
Write a function that takes in a string made up of brackets ( (, [. {. ). ]
and ] ) and other optional characters. The function should return a boolean
representing whether the string is balanced with regards to brackets.

Example:
"({[]})" => True

Optimal Complexity: O(n) || O(n)
'''

def balancedBrackets(string):
    pairs = {')':'(',']':'[','}':'{'}
    result = []

    for x in string:
        if x in pairs.values():
            result.append(x)
        elif x in pairs.keys():
            if len(result) == 0:
                return False
            elif pairs[x] == result[-1]:
                result.pop()
            else:	
                return False
    return len(result) == 0



if __name__ == '__main__': 
	print(balancedBrackets("({[]})") == True)


    
