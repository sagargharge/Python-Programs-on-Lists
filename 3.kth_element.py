# Question - 1.03 (*) Find the K'th element of a list.
# The first element in the list is number 1.

def find_kth_element(x,a):
	# validate input
	if a >= len(x):
		print "IndexOutOfRange"
	else:
		# Display the desired element from the list
		desired_element = x[a]
		print "The desired element is: " + desired_element

# Examples
x = ['a','s','d','f','g']
print x
print "\r"
a = input("Enter the desired number")
find_kth_element(x,a)

# output :
#['a', 's', 'd', 'f', 'g']

#Enter the desired number4
#The desired element is: g


#['a', 's', 'd', 'f', 'g']

#Enter the desired number5
#IndexOutOfRange

