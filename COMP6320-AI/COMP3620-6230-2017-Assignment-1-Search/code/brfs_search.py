"""
    Enter your details below:

    Name: Longfei Zhao
    Student Code: u5976992
    email: u5976992@anu.edu.au
"""

import util
from frontiers import *
from search_strategies import *

def solve(problem) :
    '''A simple BFS
    '''
    s0 = problem.get_initial_state()
    frontier = Queue()
    tempSearchNode = SearchNode(s0, action = None, path_cost = 0, parent = None, depth = 0)
    frontier.push(tempSearchNode)
    vis = set()
    path = list()
    vis.add(s0)
    while True:
        tempSearchNode = frontier.pop()
        for successor, action, cost in problem.get_successors(tempSearchNode.state) :
            if successor not in vis:
                if problem.goal_test(successor):
                    path.append(action)
                    while True:
                        path.append(tempSearchNode.action)
                        tempSearchNode = tempSearchNode.parent
                        if tempSearchNode.state == s0:
                            path.reverse()
                            return path
                vis.add(successor)
                frontier.push(SearchNode(successor, action, tempSearchNode.path_cost + cost, tempSearchNode, tempSearchNode.depth + 1))
