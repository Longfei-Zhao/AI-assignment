"""
    Enter your details below:

    Name: Longfei Zhao
    Student Code: u5976992
    email: u5976992@anu.edu.au
"""

import util
from frontiers import *
from search_strategies import *

# Check assignment handout for further details and explanations.
def solve( problem ) :
    '''I build a IDA* instead of just IDDFS to satisfy the Expanded node requirement.
    '''
    global solved, res, vis, FOUND, MAX
    FOUND = 'FOUND'
    res = None
    MAX = 10000

    s0 = problem.get_initial_state()
    startSearchNode = SearchNode(s0, None, 0, None, 0)
    path = []
    bound = h(startSearchNode, problem)

    while True:
        vis = dict()
        bound = recursive_DLS(startSearchNode, problem, 0, bound)
        if bound == FOUND:
            break
    while True:
        path.append(res.action)
        res = res.parent
        if res.state == s0:
            path.reverse()
            return path

def recursive_DLS(node, problem, depth, bound):
    '''(SearchNode, SearchProblem, int, int) -> int
    bound: Currently, the smallest possible cost.
    Return new_bound, which slowly increase bound to get the shortest path.
    '''
    global solved, res, vis, FOUND, MAX

    f = node.path_cost + h(node, problem)

    if f > bound:
        return f
    if problem.goal_test(node.state):
        res = node
        return FOUND
    if node.state not in vis or vis[node.state] > node.depth:
        vis[node.state] = node.depth
    else:
        return MAX

    newBound = MAX
    for successor, action, cost in problem.get_successors(node.state) :
        nextSearchNode = SearchNode(successor, action, node.path_cost + cost, node, node.depth + 1)
        tempBound = recursive_DLS(nextSearchNode, problem, depth + 1, bound)
        if tempBound == FOUND:
            return FOUND
        if tempBound < newBound:
            newBound = tempBound
    return newBound

def h(node, problem):
    '''(SearchNode, SearchProblem) -> int
    Get the manhattan distance between current SearchNode and end point.
    '''
    return (node.state[0] - problem.goal_pos[0]) + (node.state[1] - problem.goal_pos[1])
