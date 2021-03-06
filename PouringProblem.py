def pour_problem(X, Y, goal, start=(0,0)):
    """X and Y are the capacity of glasses; (x,y) is current filling levels
    and represents so a state. The goal is a level that can be in either glass.
    Start at start State and follow successors until we reach the goal.
    Keep track of frontier and previously explored; fail when no frontier."""
    if goal in start:
        return [start]
    explored = set() # a set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        (x,y) = path[-1] # last state in the first path of the frontier
        for (state, action) in successors(x, y, X, Y).items():
            if state not in explored: # explored means checked if goal in it.
                explored.add(state)
                path2 = path + [action, state]
                if goal in state:
                    return path2
                else:
                    frontier.append(path2)
    return  Fail

Fail = []

def successors(x, y, X, Y):
    """Return a dict of {state: action} pairs descriobing what can be reached from
    the (x,Y) state, and the action to reach it"""
    assert x <= X and y <= Y ## (x, y) is glass levels, X and Y capacity
    return {((0, y+x) if y+x <= Y else (x-(Y-y), y+(Y-y))) : 'X->Y',
            ((x+y, 0) if x+y <= X else (x+(X-x), y-(X-x))) : 'Y->X',
            (X, y) : 'fill X', (x, Y) : 'fill Y',
            (0, y) : 'empty X', (x, 0) : 'empty Y'

            }

import doctest
class Test:"""
>>> successors(0, 0, 4, 9)
{(0, 9): 'fill Y', (0, 0): 'empty Y', (4, 0): 'fill X'}

>>> successors(3, 5, 4, 9)
{(4, 5): 'fill X', (4, 4): 'Y->X', (3, 0): 'empty Y', (3, 9): 'fill Y', (0, 5): 'empty X', (0, 8): 'X->Y'}

>>> successors(3, 7, 4, 9)
{(4, 7): 'fill X', (4, 6): 'Y->X', (3, 0): 'empty Y', (0, 7): 'empty X', (3, 9): 'fill Y', (1, 9): 'X->Y'}

>>> pour_problem(4, 9, 6)
[(0, 0), 'fill Y', (0, 9), 'Y->X', (4, 5), 'empty X', (0, 5), 'Y->X', (4, 1), 'empty X', (0, 1), 'Y->X', (1, 0), 'fill Y', (1, 9), 'Y->X', (4, 6)]

## what problem, with X, Y and goal < 10 has the longest solution?
## answer: pour_problem(7, 9, 8), with 14 steps

>>> def num_actions(triplet): X, Y, goal = triplet; return len(pour_problem(X,Y,goal))
>>> max([(X, Y, goal) for X in range(1, 10) for Y in range(1, 10)
...                     for goal in range(1,max(X, Y))], key = num_actions)
(7, 9, 8)
    """

print doctest.testmod()

print