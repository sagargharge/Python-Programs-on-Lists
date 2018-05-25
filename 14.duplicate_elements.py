# Question - 1.14 (*) Duplicate the elements of a list.

def duplicate_elements(l):
  return [x for x in l for i in (1,2)]

# Example
l = ['a','a','b','b','c','c','a','a','d','d','e','e','e']
print l

print "Duplicating the whole list looks like: "
print duplicate_elements(l)

# Output
# ['a', 'a', 'b', 'b', 'c', 'c', 'a', 'a', 'd', 'd', 'e', 'e', 'e']
# Duplicating the whole list looks like:
# ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'a', 'a', 'a', 'a', 'd', 'd', 'd', 'd', 'e', 'e', 'e', 'e', 'e', 'e']
