# Question - 1.23 (**) Extract a given number of randomly selected elements from a list.

import random
def rnd_select(L, N):
	return random.sample(L, N)

# Example
l = ['a','b','c','d','e','f','g','h','i','j']
print l

i = input("Enter a number: ")

print "Random list looks like: "
print rnd_select(l,i)

# Output:-

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# Enter a number: 4
# Random list looks like: 
# ['c', 'd', 'j', 'g']

################

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# Enter a number: 4
# Random list looks like: 
# ['a', 'j', 'c', 'h']
