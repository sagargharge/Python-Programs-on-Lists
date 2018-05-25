# Question - 1.15 (**) Duplicate the elements of a list a given number of times.

def duplicatebynumber(l, n):
  return [x for x in l for i in range(n)]

# Example
l = ['a','b','c','d','e']
print l

n = input("Enter the number of times, you want to see the elements of the list to be duplicated: ")
print "Duplicating the list by your input: "
print duplicatebynumber(l,n)

# Output
# ['a', 'b', 'c', 'd', 'e']
# Enter the number of times, you want to see the elements of the list to be duplicated: 2
# Duplicating the list by your input:
# ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e', 'e']
