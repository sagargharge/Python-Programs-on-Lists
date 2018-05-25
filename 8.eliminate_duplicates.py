# Question - 1.08 (**) Eliminate consecutive duplicates of list elements.
# If a list contains repeated elements they should be replaced with a single copy of the element. # The order of the elements should not be changed.

# Examples
l = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
print l
l1 = []
for i in l:
	if i not in l1:
		l1.append(i)

print "Without duplicates, the list looks like: "
print l1


# Output.
# ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
# Without duplicates, the list looks like: 
# ['a', 'b', 'c', 'd', 'e']

