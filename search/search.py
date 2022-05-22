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

# CODE HERE!
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
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
        neighbors = problem.getSuccessors(current)

        # condition check
        if len(neighbors) > 0:
            # every neighbor nodes
            for successor in neighbors:
                # not visited
                if successor[0] not in visited:
                    paths[successor[0]] = paths[current] + [successor[1]]
                    stack.push(successor[0])
                    
    # util.raiseNotDefined()

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
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    # lowest priority
    pq = util.PriorityQueue()
    pq.push(problem.getStartState(), 0)
    
    paths = {}
    paths[problem.getStartState()] = []
    
    while (not pq.isEmpty()):
        current = pq.pop()
        
        if problem.isGoalState(current):
            return paths[current]
        
        neighbors = problem.getSuccessors(current)

        if len(neighbors) > 0:
            for successor in neighbors:
                if successor[0] not in paths.keys():
                    paths[successor[0]] = paths[current] + [successor[1]]
                    pq.push(successor[0], problem.getCostOfActions(paths[successor[0]]) + heuristic(successor[0], problem))
                else:
                    orig = problem.getCostOfActions(paths[current] + [successor[1]]) + heuristic(successor[0], problem)
                    if orig < problem.getCostOfActions(paths[successor[0]]):
                        paths[successor[0]] = paths[current] + [successor[1]]
                        pq.push(successor[0], problem.getCostOfActions(paths[successor[0]]) + heuristic(successor[0], problem))
    
    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
