# --------------
# User Instructions
#
# Complete the code for the compiler by completing the constructor
# for the patterns alt(x, y) and oneof(chars).
from functools import update_wrapper
def lit(s):
    set_s = set([s])
    return lambda Ns: set_s if len(s) in Ns else null

def alt(x, y):      return lambda Ns: x(Ns) | y(Ns)
def star(x):        return lambda Ns: opt(plus(x))(Ns)
def plus(x):        return lambda Ns: genseq(x, star(x), Ns, startx=1)  # Tricky
def oneof(chars):   return lambda Ns: set(chars) if 1 in Ns else null
def seq(x, y):      return lambda Ns: genseq(x, y, Ns)
def opt(x):         return alt(epsilon, x)
dot = oneof('?')  # You could expand the alphabet to more chars.
epsilon = lit('')  # The pattern that matches the empty string.
null = frozenset([])
# explained here https://discussions.udacity.com/t/the-evolution-of-genseq/91076
def genseq(x, y, Ns, startx=0):
    if not Ns:
        return null
    xmatches = x(set(range(startx, max(Ns) + 1)))
    Ns_x = set(len(m) for m in xmatches)
    Ns_y = set(n-m for n in Ns for m in Ns_x if n-m >= 0)
    ymatches = y(Ns_y)
    return set(m1 + m2
               for m1 in xmatches for m2 in ymatches
               if len(m1 + m2) in Ns)

#http://stackoverflow.com/questions/739654/how-to-make-a-chain-of-function-decorators-in-python/1594484#1594484
def decorator(d):
    def _d(fn):
        update_wrapper(d(fn) ,fn)

    update_wrapper(_d, d)

    return _d
# ---------------
# User Instructions
#
# Write a function, n_ary(f), that takes a binary function (a function
# that takes 2 inputs) as input and returns an n_ary function.
@decorator
def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""

    def n_ary_f(x, *args):
        return x if not args else f(x, n_ary_f(*args))

    #update_wrapper(n_ary_f, f)
    return n_ary_f



@n_ary
def test1(x,y): return  ('test1', x, y)
#test1 = n_ary(test1)
a, b, c = map(lit,['a', 'b', 'c'])
print
print help(test1)

# def test():
#     f = lit('hello')
#     assert f(set([1, 2, 3, 4, 5])) == set(['hello'])
#     assert f(set([1, 2, 3, 4])) == null
#
#     g = alt(lit('hi'), lit('bye'))
#     assert g(set([1, 2, 3, 4, 5, 6])) == set(['bye', 'hi'])
#     assert g(set([1, 3, 5])) == set(['bye'])
#
#     h = oneof('theseletters')#retruns the letter from the input if it's mentioned
#                             #at lest once in the string and if 1 is part of the lengths passed
#     assert h(set([1, 2, 3])) == set(['t', 'h', 'e', 's', 'l', 'r'])
#     assert h(set([2, 3, 4])) == null
#
#     return 'tests pass'
#
#
# f = seq(lit('a'), alt(lit('b'), lit('c')))
# print f([1,2,3])