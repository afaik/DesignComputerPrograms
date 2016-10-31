import itertools
def floor_puzzle():
    floors = bottom, _, _, _, top = [0, 1, 2, 3, 4]
    possible_floors = itertools.permutations(floors, len(floors))
    return next([Hopper, Kay, Liskov, Perlis, Ritchie]
                for Hopper, Kay, Liskov, Perlis, Ritchie in possible_floors
                if Hopper != top
                and Kay != bottom
                and Liskov not in [top, bottom]
                and Perlis - Kay > 1
                and not is_adjacent(Ritchie, Liskov)
                and not is_adjacent(Liskov, Kay)


    )


def is_adjacent(p1, p2):
    return abs(p1-p2) == 1

print floor_puzzle()