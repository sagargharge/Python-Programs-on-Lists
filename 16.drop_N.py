# Question - 1.16 (**) Drop every N'th element from a list.

def drop(L, N):
	return [x for i,x in enumerate(L) if (i+1) % N]

# Example
l = ['a','b','c','d','e']
print l

n = input("Enter the element, you want to drop: ")
print "After dropping the element the list looks like: "
print drop(l,n)

# Output:-
# ['a', 'b', 'c', 'd', 'e']
# Enter the element, you want to drop: 2
# After dropping the element the list looks like: 
# ['a', 'c', 'e']
