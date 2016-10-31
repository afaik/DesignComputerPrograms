# -------------
# User Instructions
#
# Complete the fill_in(formula) function by adding your code to
# the two places marked with ?????.
from __future__ import  division
import string, re, itertools



def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            return f
def valid(f):
    """Formula f is valid if and only if it has no
    numbers with leading zero, and evals true."""
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False

def fill_in(formula):
    "Generate all possible fillings-in of lertters in formula with digits."
    letters = ''.join(set(re.findall(r'[A-Z]', formula)))
    #print letters
    for digits in itertools.permutations('1234567890', len(letters)):
        #print digits
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)

def faster_solve(formula):
    f, letters = compile_formula(formula)
    for per in itertools.permutations((1,2,3,4,5,6,7,8,9), len(letters)):
        try:
            if f(*per):
                table = string.maketrans(letters, ''.join(map(str, per)))
                return formula.translate(table)
        except ArithmeticError:
            pass

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():

        res = '+'.join(['%s*%s' % (l, 10**pos)  for pos, l in enumerate(word[::-1])])
        return '(' + res + ')'
    else:
        return  word


def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
    in same order as parms of function. The first digit of a multi-digit
    number can't be 0. So if YOU is a word in the formula, and the function
    is called with Y eqal to 0, the function should return False."""

    letters = ''.join(set(re.findall(r'[A-Z]', formula)))
    params = ', '.join(letters)
    splitted_formula = re.split('[^A-Z]', formula)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    multi_letters = '[' + ','.join([tok[0] for tok in splitted_formula if len(tok) > 1]) + ']'
    body = ''.join(tokens)

    f = 'lambda %s : %s and 0 not in %s' % (params, body, multi_letters)
    if verbose:
        print f

    return  eval(f), letters
def test():
    assert faster_solve('A + B == BA') == None # should NOT return '1 + 0 == 01'
    assert faster_solve('YOU == ME**2') == ('289 == 17**2' or '576 == 24**2' or '841 == 29**2')
    assert faster_solve('X / X == X') == '1 / 1 == 1'
    return 'tests pass'
test()