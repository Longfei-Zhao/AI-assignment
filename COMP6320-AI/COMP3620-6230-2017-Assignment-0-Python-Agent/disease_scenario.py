""" File name:   disease_scenario.py
    Author:      Longfei Zhao
    Date:        26.2.2017
    Description: This file represents a scenario simulating the spread of an
                 infectious disease around Australia. It should be
                 implemented for Part 1 of Exercise 4 of Assignment 0.

                 See the lab notes for a description of its contents.
"""

class DiseaseScenario():
    """docstring for DiseaseScenario."""

    def __init__(self):
        self.locations = []
        self.disease = {}
        self.conn = {}

    def read_scenario_file(self, scenario_file_name):
        try:
            file = open(scenario_file_name)
            for line in file:
                info = line.split()
                keyword = info[0]
                if keyword == 'threshold':
                    self.threshold = float(info[1])
                elif keyword == 'growth':
                    self.growth = float(info[1])
                elif keyword == 'spread':
                    self.spread = float(info[1])
                elif keyword == 'location':
                    self.locations.append(info[1])
                    self.disease.setdefault(info[1], 0.0)
                    self.conn.setdefault(info[1], set())
                elif keyword == 'start':
                    self.location = info[1]
                elif keyword == 'disease':
                    self.disease[info[1]] = float(info[2])
                elif keyword == 'conn':
                    self.conn[info[1]].add(info[2])
                    self.conn[info[2]].add(info[1])
            return True
        except IOError:
            return False
    def valid_moves(self):
        ''' return a list of valid moves.
        '''
        res = []
        res.append(self.location)
        res.extend(self.conn[self.location])
        return res
    def move(self, loc):
        ''' move the agent to the specified location and clear the disease there.
        '''
        try:
            if loc in self.conn[self.location] or loc == self.location:
                self.location = loc
                self.disease[loc] = 0
            else:
                raise ValueError()
        except ValueError:
            raise
    def spread_disease(self):
        ''' spread the disease according the threshold, growth, spread, and connections between locations.
        '''
        nextDisease = self.disease.copy()
        for loc, value in nextDisease.items():
            if loc == self.location:
                value = 0.0
            else:
                value += self.disease[loc] * self.growth
                for neighbor in self.conn[loc]:
                    if self.disease[neighbor] >= self.threshold:
                        value += self.disease[neighbor] * self.spread
                nextDisease[loc] = value
        self.disease = nextDisease.copy()
