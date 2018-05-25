# Question - 1.11 (*) Modified run-length encoding.
# Modify the result of problem 1.10 in such a way that if an element has no duplicates it is simply copied into the result list. Only elements with duplicates are transferred as [N,E] terms.

from itertools import groupby
def modifiedrle(lst):
    def tmp(lg):
        if len(lg)>1:
            return [len(lg), lg[0]]
        else:
            sreturn lg[0]
    return [tmp(list(group)) for key, group in groupby(lst)]

# Example
l = ['a', 'a', 'c', 'b', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'a', 'e']
print l

print "The modified version of RUN LENGTH ENCODING looks like: "
print modifiedrle(l)

# Output
# ['a', 'c', 'd', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'a', 'e', 'a', 'e']
# The modified version of RUN LENGTH ENCODING looks like:
# [[2, 'a'], 'c', [2, 'b'], [2, 'c'], [2, 'a'], 'd', [2, 'e'], 'a', 'e']
