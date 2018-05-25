# Question - 1.12 (**) Decode a run-length encoded list.
# Given a run-length code list generated as specified in problem 1.11. Construct its uncompressed version.

from itertools import groupby
def decode_rle(lst):
    def tmp(g):
        if isinstance(g, list):
            return [(g[1], range(g[0]))]
        else:
            return [(g, [0])]
    return [x for g in lst for x, R in tmp(g) for i in R]


# Example
l = [[2, 'a'], 'c', [2, 'b'], [2, 'c'], [2, 'a'], 'd', [2, 'e'], 'a', 'e']
print l

print "The decoded version of RUN LENGTH ENCODING looks like: "
print decode_rle(l)

# Output
# ['a', 'c', 'd', 'a', 'b', [2, 'c'], [2, 'a'], 'd', 'a', 'e', 'a', 'e']
# The decoded version of RUN LENGTH ENCODING looks like:
# ['a', 'a', 'c', 'b', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'a', 'e']
