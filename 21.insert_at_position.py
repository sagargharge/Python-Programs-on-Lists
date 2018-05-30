# Question - 1.21 (**) Insert an element at a given position into a list.

def insert_at(x, L, N):
	return L[:N-1]+[x]+L[N-1:]

# Example
l = ['a','b','c','d','e','f','g','h','i','j']
print l

i = raw_input("Enter the element, you want to insert: ")
j = input("Enter the position of insertion: ")

print "The modified list looks like: "
print insert_at(i,l,j)

# Output:-
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# Enter the element, you want to insert: z
# Enter the position of insertion: 5
# The modified list looks like: 
# ['a', 'b', 'c', 'd', 'z', 'e', 'f', 'g', 'h', 'i', 'j']

