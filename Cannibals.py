# -----------------
# User Instructions
#
# Write a function, csuccessors, that takes a state (as defined below)
# as input and returns a dictionary of {state:action} pairs.
#
# A state is a tuple with six entries: (M1, C1, B1, M2, C2, B2), where
# M1 means 'number of missionaries on the left side.'
#
# An action is one of the following ten strings:
#
# 'MM->', 'MC->', 'CC->', 'M->', 'C->', '<-MM', '<-MC', '<-M', '<-C', '<-CC'
# where 'MM->' means two missionaries travel to the right side.
#
# We should generate successor states that include more cannibals than
# missionaries, but such a state should generate no successors.

def csuccessors(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    M1, C1, B1, M2, C2, B2 = state
    # your code here
    if C2 > M2 > 0 or C1 > M1 >0:
        return {}
    else:
        if B1 > 0:  # boat is on first side
            movlist = dict([((M1-i, C1-j, 0, M2+i, C2+j, B2+B1), 'M'*i + 'C'*j + '->')
                       for i in range(0,M1+1) for j in range(0,C1+1) if i + j in (1, 2)]
                           )

        if B2 > 0:
            movlist = dict([((M1+i, C1+j, B1+B2, M2-i, C2-j, 0), '<-' + 'M' * i + 'C' * j )
                            for i in range(0, M2 + 1) for j in range(0, C2 + 1) if i + j in (1, 2)]
                           )

        #print movlist
        return  movlist

Fail = []
def mc_problem(start=(3, 3, 1, 0, 0, 0), goal=None):

    if not goal:
        goal = (0, 0, 0) + start[:3]
    if goal in start:
        return [start]
    frontier = [[start]]
    explored = set()
    while(frontier):
        path = frontier.pop()
        final_state = path[-1]
        if goal == final_state:
            return path
        if final_state not in explored:
            explored.add(final_state)
            for state, action in csuccessors(final_state).items():
                path2 = path + [action, state]
                frontier.append(path2)
    return Fail

def test_csuccessors():
    assert csuccessors((2, 2, 1, 0, 0, 0)) == {(2, 1, 0, 0, 1, 1): 'C->',
                                               (1, 2, 0, 1, 0, 1): 'M->',
                                               (0, 2, 0, 2, 0, 1): 'MM->',
                                               (1, 1, 0, 1, 1, 1): 'MC->',
                                               (2, 0, 0, 0, 2, 1): 'CC->'}
    assert csuccessors((1, 1, 0, 4, 3, 1)) == {(1, 2, 1, 4, 2, 0): '<-C',
                                               (2, 1, 1, 3, 3, 0): '<-M',
                                               (3, 1, 1, 2, 3, 0): '<-MM',
                                               (1, 3, 1, 4, 1, 0): '<-CC',
                                               (2, 2, 1, 3, 2, 0): '<-MC'}
    assert csuccessors((1, 4, 1, 2, 2, 0)) == {}
    return 'tests pass'


def test_mc_problem():
    assert mc_problem() == [(3, 3, 1, 0, 0, 0), 'MC->',
                            (2, 2, 0, 1, 1, 1), '<-M',
                            (3, 2, 1, 0, 1, 0), 'CC->',
                            (3, 0, 0, 0, 3, 1), '<-C',
                            (3, 1, 1, 0, 2, 0), 'MM->',
                            (1, 1, 0, 2, 2, 1), '<-MC',
                            (2, 2, 1, 1, 1, 0), 'MM->',
                            (0, 2, 0, 3, 1, 1), '<-C',
                            (0, 3, 1, 3, 0, 0), 'CC->',
                            (0, 1, 0, 3, 2, 1), '<-C',
                            (0, 2, 1, 3, 1, 0), 'CC->',
                            (0, 0, 0, 3, 3, 1)]
    assert mc_problem((2, 1, 1, 0,0,0)) == [(2, 1, 1, 0, 0, 0), 'MC->',
                                            (1, 0, 0, 1, 1, 1), '<-M',
                                            (2, 0, 1, 0, 1, 0), 'MM->',
                                            (0, 0, 0, 2, 1, 1)]

    return 'passed mc'

def test():
    test_csuccessors()
    test_mc_problem()
print test()
