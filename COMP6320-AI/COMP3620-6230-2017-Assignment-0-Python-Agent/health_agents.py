""" File name:   health_agents.py
    Author:      Longfei Zhao
    Date:        27.2.2017
    Description: This file contains agents which fight disease. It is used
                 in Exercise 4 of Assignment 0.
"""

import random

class HealthAgent(object):
    """ A simple disease fighting agent. """

    def __init__(self, locations, conn):
        """ This contructor does nothing except save the locations and conn.
            Feel free to overwrite it when you extend this class if you want
            to do some initial computation.

            (HealthAgent, [str], { str : set([str]) }) -> None
        """
        self.locations = locations
        self.conn = conn

    def choose_move(self, location, valid_moves, disease, threshold, growth, spread):
        """ Using given information, return a valid move from valid_moves.
            Returning an inalid move will cause the system to stop.

            Changing any of the mutable parameters will have no effect on the operation
            of the system.

            This agent will locally move to the highest disease, of there is
            is no nearby disease, it will act randomly.

            (HealthAgent, str, [str], [str], { str : float }, float, float, float) -> str
        """

        max_disease = None
        max_move = None
        for move in valid_moves:
           if max_disease is None or disease[move] > max_disease:
               max_disease = disease[move]
               max_move = move

        if not max_disease:
            return random.choice(valid_moves)

        return max_move

#Make a new agent here called SmartHealthAgent, which extends HealthAgent and acts a bit more sensibly
class SmartHealthAgent(HealthAgent):
    def __init__(self, locations, conn):
        self.locations = locations
        self.conn = conn
        self.path = []
        self.threshold = 0
        self.growth = 0
        self.spread = 0
        self.pos = 1

        ''' Abandoned: Get the steps between any two locations

            self.vis = []
            self.steps = {}
            for loc in self.locations:
                self.steps[loc] = {}
            for startLoc in self.locations:
                for endLoc in self.locations:
                    if startLoc == endLoc:
                        self.steps[startLoc][endLoc] = 0
                    else:
                        self.steps[startLoc][endLoc] = -1
            for startLoc in self.locations:
                start = 0
                self.vis = []
                self.vis.append(startLoc)
                while True:
                    curLoc = self.vis[start]
                    for nextLoc in self.conn[curLoc]:
                        if nextLoc not in self.vis:
                            self.vis.append(nextLoc)
                            if self.steps[startLoc][nextLoc] == -1:
                                self.steps[startLoc][nextLoc] = self.steps[startLoc][curLoc] + 1
                    start += 1
                    if start == len(self.vis) - 1:
                        break
        '''

    def next_disease(self, disease, location):
        newDisease = disease.copy()
        newDisease[location] = 0
        nextDisease = newDisease.copy()
        for loc, value in nextDisease.items():
            if loc == location:
                continue
            else:
                value += newDisease[loc] * self.growth
                for neighbor in self.conn[loc]:
                    if newDisease[neighbor] >= self.threshold:
                        value += newDisease[neighbor] * self.spread
                nextDisease[loc] = value
        return nextDisease

    ''' Abandoned: old search function

        def depth_limit_search(self, location, valid_moves, disease, depth, threshold, growth, spread):
            self.threshold = threshold
            self.growth = growth
            self.spread = spread

            maxMove = None
            maxEvaluate = -1
            for move in valid_moves:
                self.sonMaxEvaluate = -1
                nextDisease = self.next_disese(disease, move)
                tempEvaluate =  self.recursive_DLS(move, nextDisease, depth)
                if tempEvaluate <= maxEvaluate or maxEvaluate == -1:
                    if tempEvaluate == maxEvaluate and move == location:
                        continue
                    maxEvaluate = tempEvaluate
                    maxMove = move
            return maxMove

        def recursive_DLS(self, location, disease, depth):
            if depth == 0:
                tempEvaluate = self.evaluate(disease, location)
                if tempEvaluate <= self.sonMaxEvaluate or self.sonMaxEvaluate == -1:
                    self.sonMaxEvaluate = tempEvaluate
            else:
                validMoves = self.valid_move(location)
                for move in validMoves:
                    nextDisease = self.next_disese(disease, move)
                    self.recursive_DLS(move, nextDisease, depth - 1)
            return self.sonMaxEvaluate
    '''

    def choose_move(self, location, valid_moves, disease, threshold, growth, spread):

        ''' Search - BFS
            if path:
                print next path
            else:
                find the path to all disease is 0
        '''
        if self.path:
            self.pos += 1
            if self.pos == len(self.path):
                self.pos = 1
            return self.path[self.pos]

        self.threshold = threshold
        self.growth = growth
        self.spread = spread

        queue = []
        tempPath = []
        tempPath.append(location)
        tempDisease = disease
        queue.append((tempPath, tempDisease))

        while True:
            tempPath, tempDisease = queue.pop(0)
            tempLoc = tempPath[-1]
            for move in self.conn[tempLoc]:
                nextPath = tempPath.copy()
                nextPath.append(move)
                nextDisease = self.next_disease(tempDisease, move)
                value = sum(nextDisease.values())
                if value == 0:
                    self.path = nextPath
                    return self.path[self.pos]
                queue.append((nextPath, nextDisease))

        ''' evaluate mothod - abandoned

            max_disease = None
            max_loc = location
            max_move = None
            for move in valid_moves:
                val = self.value(move, disease, growth, spread)
                if max_disease is None or val > max_disease:
                    max_disease = val
                    max_move = move
            if not max_disease:
                return random.choice(valid_moves)
            return max_move

            old search function - abandoned

            depth = 2
            move = self.depth_limit_search(location, valid_moves, disease, depth, threshold, growth, spread)
            return move
        '''
