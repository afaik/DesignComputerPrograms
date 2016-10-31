# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    text = str.lower(text)
    a, b = 0, 0
    text_len = len(text)
    for center in range(text_len):
        start = center - 1
        end = center + 1
        while(start >= 0 and end <= text_len - 1):
            if text[start] == text[end]:
                if end-start > b-a:
                    a = start
                    b = end
                start -= 1
                end += 1
            elif text[center] == text[end]:
                if end-center > b-a:
                    a = center
                    b = end
                end += 1
            else:
                break
    if b !=0:
        b += 1
    return  (a,b)





def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8, 21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    assert L('zzcbaxxabc') == (2, 10)
    return 'tests pass'


print test()