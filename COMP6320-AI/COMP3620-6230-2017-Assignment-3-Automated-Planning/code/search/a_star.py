
"""
COMP3620-6320 Artificial Intelligence 2017 - Planning Assignment Q2

Enter your details below:

Name: Longfei Zhao
Student Code: u5976992
email: u5976992@anu.edu.au


Implements the A* (a-star) search algorithm for planning.

Method to be implemented is a_star.

We import some basic data-structure that can be useful to tackle the problem.
Have a look at *heapq* that is an efficient implementation of a priority queue using a heap data-structure
Have a look at searchspace that gives you an implementation of a searchnode. In particular look at make_root_node and make_child_node
"""

import heapq
import logging

from search import searchspace
from planning_task import Task
from heuristics import BlindHeuristic



def a_star(task, heuristic=BlindHeuristic):
    """
    Searches for a plan in the given task using A* search.

    @param task The task to be solved
    @param heuristic  A heuristic callable which computes the estimated steps
                      from a search node to reach the goal.
    """
    startSearchNode = searchspace.make_root_node(task.initial_state)
    heap = []
    h0 = heuristic(startSearchNode)
    count = 0
    heapq.heappush(heap, (h0, count, startSearchNode))
    count += 1
    nodeCount = 0
    vis = set()
    res = None

    while heap:
        tempH, _, tempSearchNode = heapq.heappop(heap)
        nodeCount += 1
        if tempSearchNode.state in vis:
            continue
        vis.add(tempSearchNode.state)
        if res and res.g <= tempH:
            break
        for action, state in Task.get_successor_states(task, tempSearchNode.state):
            nextSearchNode = searchspace.make_child_node(tempSearchNode, action, state)
            if Task.goal_reached(task, state):
                if res and res.g <= nextSearchNode.g:
                    continue
                res = nextSearchNode
            else:
                count += 1
                heapq.heappush(heap, (nextSearchNode.g + heuristic(nextSearchNode), count, nextSearchNode))
    logging.info("Node Expansion: " + str(nodeCount))
    return res.extract_solution()
