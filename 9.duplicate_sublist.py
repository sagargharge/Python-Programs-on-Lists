# Question - 1.09 (**) Pack consecutive duplicates of list elements into sublists.
# If a list contains repeated elements they should be placed in separate sublists.

from itertools import groupby
def pack(lst):
    return [list(group) for key, group in groupby(lst)]


# Examples
l = ['a','c','d','a','b','c','c','a','a','d','a','e','a','e']
print l

print "The list of duplicate lists looks like: "
#print sublist_duplicates(l)
print pack(l)


# Output.
# ['a', 'c', 'd', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'a', 'e', 'a', 'e']
# The list of duplicate lists looks like:
# [['a'], ['c'], ['d'], ['a'], ['b'], ['c', 'c'], ['a', 'a'], ['d'], ['a'], ['e'], ['a'], ['e']]
