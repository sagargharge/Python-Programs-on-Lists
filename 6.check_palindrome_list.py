# Question - 1.06 (*) Find out whether a list is a palindrome.
# A palindrome can be read forward or backward; e.g. [x,a,m,a,x].

def check_palindrome_list(list_):
	# validate input type
	if not isinstance(list_, list):
		print("Input should be a list")
	else:
		# reverse list
		rev_list = list_[::-1]
		if list_ == rev_list:
			print("Yes. Given list {0} is palindrome".format(list_))
		else:
			print("No. Given list {0} is not a palindrome".format(list_))


# Examples

check_palindrome_list(['x','a','m','a','x'])

# output :
# Yes. Given list ['x', 'a', 'm', 'a', 'x'] is palindrome

check_palindrome_list(['x','a','m','a'])
# output :
# No. Given list ['x', 'a', 'm', 'a'] is not a palindrome