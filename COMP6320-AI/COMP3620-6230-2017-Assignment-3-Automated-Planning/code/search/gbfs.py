
"""
COMP3620-6320 Artificial Intelligence 2017 - Planning Assignment Q1
Classes for representing a STRIPS planning task and capturing its semantics

Enter your details below:

Name: Longfei Zhao
Student Code: u5976992
email: u5976992@anu.edu.au

Implements the Greedy Best First Search (GBFS) search algorithm for planning.

Method to be implemented is gbfs.

We provide imports for some basic data-structure that can be useful to tackle the problem. In particular have a look at heapq that
is an efficient implementation of a priority queue using heap
"""



import heapq
import logging

from search import searchspace
from planning_task import Task
from heuristics import BlindHeuristic
def gbfs(task, heuristic=BlindHeuristic):
    """
    Searches for a plan in the given task using Greedy Best First Search search.

    @param task The task to be solved
    @param heuristic  A heuristic callable which computes the estimated steps
                      from a search node to reach the goal.
    """

    startSearchNode = searchspace.make_root_node(task.initial_state)
    heap = []
    heapq.heappush(heap, (heuristic(startSearchNode), 0, startSearchNode))
    count = 0
    res = None
    nodeCount = 0
    vis = set()
    while True:
        if not heap:
            return 0
        _, _, tempSearchNode = heapq.heappop(heap)
        nodeCount += 1
        if tempSearchNode.state in vis:
            continue
        vis.add(tempSearchNode.state)
        for action, state in Task.get_successor_states(task, tempSearchNode.state):
            nextSearchNode = searchspace.make_child_node(tempSearchNode, action, state)
            if Task.goal_reached(task, state):
                logging.info("Node Expansion: " + str(nodeCount))
                return nextSearchNode.extract_solution()
            else:
                count += 1
                heapq.heappush(heap, (heuristic(nextSearchNode), count, nextSearchNode))
