# -----------
# User Instructions
# 
# Modify the test() function to include three new test cases.
# These should assert that hand_rank gives the appropriate
# output for the given straight flush, four of a kind, and
# full house.
#
# For example, calling hand_rank on sf should output (8, 10)
#
# Since the program is still incomplete, clicking RUN won't do 
# anything, but clicking SUBMIT will let you know if you
# have gotten the problem right. 
import random
import itertools

hand_names = ['High Cards', 'One Pair', 'Two Pair', '3 of a Kind', 'Straight', 'Flush', 'Full House', '4 of a Kind', 'Straight Flush']
def poker(hands):
    "Return the list of best hands: poker([hand,...]) => [hand, hand..]"
    return allmax(hands, key=hand_rank)

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush (D9 D8 D7 D6 D5)->(8, 9)
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind (9 9 9 9 3) -> (7, 9, 3)
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house (4 4 4 5 5) -> (6, 4, 5)
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush ( DA D9 D5 D3 D2)->(5, (10 9 5 3 2))
        return (5, ranks)
    elif straight(ranks):                          # straight ( 7 6 5 4 3)->(4, (7 6 5 4 3))
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind ( 7 7 7 8 6) (3, 7,(7 6 5 4 3))
        return (3, kind(3, ranks), ranks)
    elif two_pairs(ranks):                          # 2 pair (6 6 5 5 8) (2,(6,5),(6 6 5 5 8))
        return (2, two_pairs(ranks) , ranks)
    elif kind(2, ranks):                           # kind (4, 4 , 8, 3, 7) (1, 4, (4 4 8 3 7))
        return (1, kind(2, ranks), ranks)
    else:                                          # high card (3 5 7 9 12) (0, (3 5 7 9 12))
        return (0, ranks)

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in cards]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if ranks == [14, 5, 4, 3, 2] else ranks

def straight(ranks): # 9 8 7 6 5
    return max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5

def flush(hand): #
    return len(set([s for r,s in hand])) == 1

def kind(n, ranks):
    for r in ranks:
        if ranks.count(r) == n: return r
    return  None

def two_pairs(ranks):
    "If there are two pair here, return the two ranks of the two pairs, else None."
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

mydeck = [r + s for r in '23456789TJQKA' for s in 'SHDC']
wikipedia_values = [50.1, 42.3, 4.75, 2.11, 0.392, 0.197, 0.144, 0.0240, 0.00139, 0.000154]


def deal(numhands, n=5, deck=mydeck):
    # Your code here.
    random.shuffle(deck)
    return [deck[n*i : n*(i+1)] for i in range(numhands)]

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    # Your code here.
    if key == None:
        key = lambda x: x
    max_hand_rank = key(max(iterable, key=key))
    return [hand for hand in iterable if key(hand) == max_hand_rank]

def hand_percentage(n = 700*1000):
    counts = [0] * 9
    for i in range(n/10):
        for hand in  deal(10):
            ranking = hand_rank(hand)[0]
            if ranking == 8:
                print ranking

            counts[ranking] += 1

    for i in reversed(range(9)):
        print("%14s: %6.6f %% %6.6f %%" % (hand_names[i], 100.0 * counts[i] / n, wikipedia_values[i]))


def test_best_hand():
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'





def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand."
    return max(itertools.combinations(hand, 5), key = hand_rank)

def test():
    allmaxlist = [['6C', '7C', '8C', '9C', 'TC'], ['6D', '7D', '8D', '9D', 'TD'],
                    ['9D', '9H', '9S', '9C', '7D'], ['TD', 'TC', 'TH', '7C', '7D']]
    assert allmax(allmaxlist, hand_rank) == [['6C', '7C', '8C', '9C', 'TC'], ['6D', '7D', '8D', '9D', 'TD']]
    "Test casesfor the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "5S 5D 9H 9C 6S".split()  # Two pairs
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 9, 8, 7, 4]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)

allranks = '23456789TJQKA'
redcards = [r+s for r in allranks for s in 'DH']
blackcards = [r+s for r in allranks for s in 'SC']

def best_wild_hand(hand):
    # https://discussions.udacity.com/t/best-wild-hand-hw1-2-solution/65955/5
    "Try all values for jokers in all 5-card selections."
    hands = set(best_hand(h)
                for h in itertools.product(*map(replacements, hand)))
    return max(hands, key = hand_rank)


def replacements(card):
    if card == '?B' : return blackcards
    elif card == '?R': return redcards
    else: return [card]

def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'
print test_best_hand()
print best_wild_hand("6C 7C 8C 9C TC 5C ?B".split())
