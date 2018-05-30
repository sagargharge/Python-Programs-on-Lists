# Question - 1.19 (**) Rotate a list N places to the left.

def rotate(L, N):
	return L[N:] + L[:N]

# Example
l = ['a','b','c','d','e','f','g','h','i','j']
print l

i = input("by how many places do you want to rotate the list: ")

print "The rotated list looks like: "
print rotate(l,i)

# Output:-
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# by how many places do you want to rotate the list: 4
# The rotated list looks like: 
# ['e', 'f', 'g', 'h', 'i', 'j', 'a', 'b', 'c', 'd']
# 
