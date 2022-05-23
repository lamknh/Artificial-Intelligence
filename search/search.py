# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    # return start state of search problem
    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    # return true of valid goal
    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    # return (successor, action, stepCost)
    # State: (5, 5) then Start's successors: [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    # return total cost of certain action
    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    # DFS uses stack
    stack = util.Stack()
    # initial state into stack
    stack.push(problem.getStartState())
    
    # DFS
    visited = []
    visited.append(problem.getStartState())
    
    paths = {}
    paths[problem.getStartState()] = []
    
    # DFS actions
    while (not stack.isEmpty()):
        current = stack.pop()
        # visit check
        visited.append(current)
        
        # reaches goal -> return path
        if problem.isGoalState(current):
            return paths[current]
        
        # (successor, action, stepCost)
        neighbors = problem.getSuccessors(current)
        
        for successor in neighbors:
            # not visited
            if successor[0] not in visited:
                # successor[0] = successor / successor[1] = action : find path
                # save path
                paths[successor[0]] = paths[current] + [successor[1]]
                # DFS
                stack.push(successor[0])

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

# heuristic = distance
def aStarSearch(problem, heuristic=nullHeuristic):
    visited = []
    # longest distance as possible
    pq = util.PriorityQueue()
    paths = []
    
    pq.push((problem.getStartState(), paths), 0)
    
    # A* Search
    while not pq.isEmpty():
        next_node, paths = pq.pop()
        
        # reaches goal
        if problem.isGoalState(next_node):
            return paths
        
        # not searched node
        if next_node not in visited:
            successors = problem.getSuccessors(next_node)
            for child in successors:
                if child[0] not in visited:
                    # A* Search
                    # heuristic = distance method
                    cost = problem.getCostOfActions(paths + [child[1]]) + heuristic(child[0], problem)
                    pq.push((child[0], paths + [child[1]]), cost)
                    
        visited.append(next_node)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
