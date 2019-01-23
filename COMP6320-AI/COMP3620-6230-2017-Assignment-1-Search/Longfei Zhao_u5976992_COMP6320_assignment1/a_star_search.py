"""
    Enter your details below:

    Name: Longfei Zhao
    Student Code: u5976992
    email: u5976992@anu.edu.au
"""

import util
from frontiers import *
from search_strategies import *
from heuristics import *


def solve(problem, heuristic) :
    """ *** YOUR CODE HERE *** """

    s0 = problem.get_initial_state()
    frontier = PriorityQueue()
    startSearchNode = SearchNode(s0, action = None, path_cost = 0, parent = None, depth = 0)
    h0 = heuristic(s0, problem)
    frontier.push(startSearchNode, h0)
    path = list()
    vis = dict()
    vis[s0] = h0
    res = None

    while True:
        if frontier.is_empty():
            break
        tempSearchNode = frontier.pop()
        tempF = tempSearchNode.path_cost + heuristic(tempSearchNode.state, problem)
        if res and res.path_cost <= tempF:
            break
        for successor, action, cost in problem.get_successors(tempSearchNode.state) :
            nextSearchNode = SearchNode(successor, action, tempSearchNode.path_cost + cost, tempSearchNode, tempSearchNode.depth + 1)
            if problem.goal_test(successor):
                if res and tempSearchNode.path_cost + cost >= res.path_cost:
                    continue
                res = nextSearchNode
            tempF = tempSearchNode.path_cost + cost + heuristic(successor, problem)
            if successor not in vis or vis[successor] > tempF:
                vis[successor] = tempF
                frontier.push(nextSearchNode, tempF)
    while True:
        path.append(res.action)
        res = res.parent
        if res.state == s0:
            path.reverse()
            return path
