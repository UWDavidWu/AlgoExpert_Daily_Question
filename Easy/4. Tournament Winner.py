'''
Date: 2021/12/17
Author: David Wu
Link: https://www.algoexpert.io/questions/Tournament%20Winner

Question Summary:

  Given an array of pairs representing the teams that have competed against each
  other and an array containing the results of each competition, write a
  function that returns the winner of the tournament.
  

Example:
 [["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]], [0, 0, 1] => 'Python'
]

Optimal Complexity: O(n) || O(c)
'''

import operator
def tournamentWinner(competitions, results):

    teamPoints = {}
    results = [score-1 for score in results]

    for index,x in enumerate(competitions):
        winningTeam = x[results[index]] 
        
        if winningTeam not in teamPoints:
            teamPoints[winningTeam] = 0
        teamPoints[winningTeam] += 3

    return max(teamPoints.items(), key=operator.itemgetter(1))[0]

if __name__ == '__main__':
    testArray1 = [  ["HTML", "C#"],
                    ["C#", "Python"],
                    ["Python", "HTML"]  ]
    testArray2 = [0, 0, 1]
    
    print(tournamentWinner(testArray1, testArray2) == "Python")
    
