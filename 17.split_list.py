# Question - 1.17 (**) Split a list into two parts; the length of the first part is given.

def split(L, N):
	return L[:N], L[N:]

# Example
l = ['a','b','c','d','e']
print l

n = input("Enter the position, after which you want to split: ")
print "After splitting the list looks like: "
print split(l,n)

# Output:-
# ['a', 'b', 'c', 'd', 'e']
# Enter the position, after which you want to split: 2
# After splitting the list looks like: 
# (['a', 'b'], ['c', 'd', 'e'])
