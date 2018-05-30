# Question - 1.18 (**) Extract a slice from a list.
#Given two indices, I and K, the slice is the list containing the elements between the I'th and  K'th element of the original list (both limits included). Start counting the elements with 1.

def slice(L, I, K):
	return L[I-1:K]

# Example
l = ['a','b','c','d','e','f','g','h','i','j']
print l

i = input("Enter first interval: ")
k = input("Enter second interval: ")
print "The sliced list looks like: "
print slice(l,i,k)

# Output:-
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# Enter first interval: 3
# Enter second interval: 6
# The sliced list looks like: 
# ['c', 'd', 'e', 'f']
