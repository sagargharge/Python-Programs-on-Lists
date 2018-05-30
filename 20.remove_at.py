# Question - 1.20 (**) Remove the K'th element from a list.

def remove_at(L, N):
	return L[N-1], L[:N-1] + L[N:]

# Example
l = ['a','b','c','d','e','f','g','h','i','j']
print l

i = input("Enter the position of the element, you want to remove: ")

print "The modified list looks like: "
print remove_at(l,i)

# Output:-
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# Enter the position of the element, you want to remove: 3
# The modified list looks like: 
# ('c', ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

