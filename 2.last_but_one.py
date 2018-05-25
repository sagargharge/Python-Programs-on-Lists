# Question - 1.02 (*) Find the last but one element of a list.
# (de: zweitletztes Element, fr: avant-dernier élément)

def least_but_one(list_):
	# validate input type
	if len(list_)==0:
		print "The list is empty"
	else:
		# Display the last element of the list
		last_element = list_[-2]
		print "The last but one element is: " + last_element

# Examples

least_but_one(['a','s','d','f','g'])

# output :
# The last but one element is: f

