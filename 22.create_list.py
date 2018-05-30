# Question - 1.22 (**) Create a list containing all integers within a given range.

def irange(I, J):
	return range(I, J+1)

# Example

i = input("Enter lower bound: ")
j = input("Enter upper bound: ")

print "The newly created list looks like: "
print irange(i,j)

# Output:-
# Enter lower bound: 5
# Enter upper bound: 10
# The newly created list looks like: 
# [5, 6, 7, 8, 9, 10]
