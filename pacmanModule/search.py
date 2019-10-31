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

from . import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

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
    open_stack = util.Stack()
    closed =[]
    open_stack.push((problem.getStartState(), []))
    while (not open_stack.isEmpty()):
        state, path = open_stack.pop()
        if problem.isGoalState(state):
            return path
        x_children = problem.getSuccessors(state)
        closed.append(state)
        for child in x_children:
            if child[0] not in closed and len(list(filter(lambda x:child[0] in x, open_stack.list))) == 0 : # check if in open and close
                open_stack.push((child[0], path+[child[1]]))
    return False

def breadthFirstSearch(problem):
    open_queue = util.Queue() 
    open_queue.push((problem.getStartState(), [])) 
    closed = [] 
    while (not open_queue.isEmpty()): 
        state, path = open_queue.pop() 
        if problem.isGoalState(state):
            return path 
        x_children = problem.getSuccessors(state) 
        closed.append(state) 
        for child in x_children: 
            if child[0] not in closed and len(list(filter(lambda x:child[0] in x, open_queue.list))) == 0 : # check if in open and close 
                open_queue.push((child[0], path + [child[1]])) 
    return False 

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

def bestFirstSearch(problem):
    open_queue = util.PriorityQueue() 
    priority = util.manhattanDistance(problem.getStartState(), problem.goal)
    # print(priority)
    open_queue.push((problem.getStartState(), []), priority) 
    close_queue = util.Queue() 
    while open_queue.isEmpty() is not True: 
        x, path = open_queue.pop() 
        if problem.isGoalState(x): 
            return path 
        else: 
            x_children = problem.getSuccessors(x) 
            for child in x_children: 
  
                for y in [item for item in open_queue.heap if child[0] in item]: 
                    if(len(path) + 1 < len(y[1])): 
                        y[1] = path + [child[1]] 
                        print("current < opened") 
 
                for y in [item for item in close_queue.list if child[0] in item]: 
                    if(len(path) + 1 < len(y[1])): 
                        newPath =  path + [child[1]] 
                        newState = y[0]
                        newPriority = util.manhattanDistance(newState, problem.goal)
                        open_queue.push((newState, newPath), newPriority)
                        close_queue.list.remove(y)
                        print("current < closed") 
 
                if len(list(filter(lambda x:child[0] in x, open_queue.heap))) == 0 and len(list(filter(lambda x:child[0] in x, close_queue.list))) == 0: 
                #if child[0] not in open_queue.heap and child not in close_queue.list: 
                    child_priority =  util.manhattanDistance(child[0], problem.goal) # astar: include len(path)+1 | best first search: leave len(path)+1 out
                    # print(child_priority)
                    open_queue.push((child[0], path + [child[1]]), child_priority)
                    

                
        close_queue.push((x, path)) 
    return False 

def aStarSearch(problem): 
    open_queue = util.PriorityQueue() 
    priority = util.manhattanDistance(problem.getStartState(), problem.goal)
    # print(priority)
    open_queue.push((problem.getStartState(), []), priority) 
    close_queue = util.Queue() 
    while open_queue.isEmpty() is not True: 
        x, path = open_queue.pop() 
        if problem.isGoalState(x): 
            return path 
        else: 
            x_children = problem.getSuccessors(x) 
            for child in x_children: 
  
                for y in [item for item in open_queue.heap if child[0] in item]: 
                    if(len(path) + 1 < len(y[1])): 
                        y[1] = path + [child[1]] 
                        print("current < opened") 
 
                for y in [item for item in close_queue.list if child[0] in item]: 
                    if(len(path) + 1 < len(y[1])): 
                        newPath =  path + [child[1]] 
                        newState = y[0]
                        newPriority = len(newPath) + util.manhattanDistance(newState, problem.goal)
                        open_queue.push((newState, newPath), newPriority)
                        close_queue.list.remove(y)
                        print("current < closed") 
 
                if len(list(filter(lambda x:child[0] in x, open_queue.heap))) == 0 and len(list(filter(lambda x:child[0] in x, close_queue.list))) == 0: 
                #if child[0] not in open_queue.heap and child not in close_queue.list: 
                    child_priority = (len(path)+1) + util.manhattanDistance(child[0], problem.goal) # astar: include len(path)+1 | best first search: leave len(path)+1 out
                    # print(child_priority)
                    open_queue.push((child[0], path + [child[1]]), child_priority)
                    

                
        close_queue.push((x, path)) 
    return False 

# def manhattanHeuristic(position, problem, info={}):
#     "The Manhattan distance heuristic for a PositionSearchProblem"
#     xy1 = position
#     xy2 = problem.goal
#     return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
bestfs = bestFirstSearch
