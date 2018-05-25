# Question - 1.01 (*) Find the last element of a list.

def find_last_element(list_):
	# validate input type
	if len(list_)==0:
		print "The list is empty"
	else:
		# Display the last element of the list
		last_element = list_[-1]
		print "The lase element is: " + last_element


find_last_element(['a','s','d','f','g'])

# output :
# The lase element is: g

