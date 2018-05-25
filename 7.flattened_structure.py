# Question - 1.07 (**) Flatten a nested list structure.
# Transform a list, possibly holding lists as elements into a 'flat' list by replacing each list 
# with its elements (recursively).

L = [[[1, [2, 3]], [[4], [5]], [6]], [7,[8,9]], 10]
print L
print "List in a generatised/flattened form, looks like: "

x=[]

def flattened_structure(L):
	for ele in L:
		if type(ele) is list:
			flattened_structure(ele)	
		else:
			x.append(ele)

flattened_structure(L)
print x


# output :
# [[[1, [2, 3]], [[4], [5]], [6]], [7, [8, 9]], 10]
# List in a generatised/flattened form, looks like: 
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

