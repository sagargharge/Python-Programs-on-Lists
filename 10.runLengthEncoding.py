# Question - 1.10 (*) Run-length encoding of a list.
# Use the result of problem 1.09 to implement the so-called run-length encoding data compression
# method. Consecutive duplicates of elements are encoded as terms [N,E] where N is the number of
# duplicates of the element E.

from itertools import groupby
def runLengthEncoding(lst):
    return [[len(list(group)), key] for key, group in groupby(lst)]


# Example
l = ['a', 'a', 'c', 'b', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'a', 'e']
print l

print "The RUN LENGTH ENCODING looks like: "
print runLengthEncoding(l)

# Output
# ['a', 'c', 'd', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'a', 'e', 'a', 'e']
# The RUN LENGTH ENCODING looks like:
# [[2, 'a'], [1, 'c'], [2, 'b'], [2, 'c'], [2, 'a'], [1, 'd'], [2, 'e'], [1, 'a'], [1, 'e']]
