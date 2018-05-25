# Question - 1.13 (**) Run-length encoding of a list (direct solution).
# Implement the so-called run-length encoding data compression method directly. I.e. dont explicitly create the sublists containing the duplicates, as in problem 1.09, but only count them. As in problem 1.11, simplify the result list by replacing the singleton terms [1,X] by X.


from itertools import groupby
def rle_direct(lst):
    def tmp(k, g):
        l = len(list(g))
        if l>1:
            return [l, k]
        else:
            return k
    return [tmp(key, group) for key, group in groupby(lst)]


# Example
l = ['a','a','c','b','b','c','c','a','a','d','e','e','a','e']
print l

print "The RUN LENGTH ENCODING by direct method: "
print rle_direct(l)

# Output
# ['a', 'a', 'c', 'b', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'a', 'e']
# The RUN LENGTH ENCODING by direct method:
# [[2, 'a'], 'c', [2, 'b'], [2, 'c'], [2, 'a'], 'd', [2, 'e'], 'a', 'e']
