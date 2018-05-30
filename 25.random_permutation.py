# Question - 1.25 (**) Generate a random permutation of the elements of a list.

import random

def rnd_permu(L):
        result = list(L)
        random.shuffle(result)
        return result

# Example
l = ['a','b','c','d','e','f','g','h','i','j']
print l

print "\r"

print "The random list looks like: "
print rnd_permu(l)

# Output:-

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# The random list looks like: 
# ['a', 'b', 'g', 'f', 'c', 'j', 'e', 'i', 'd', 'h']

##################

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# The random list looks like: 
# ['g', 'f', 'c', 'h', 'a', 'j', 'e', 'b', 'i', 'd']
