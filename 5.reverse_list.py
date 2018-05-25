# Question - 1.05 (*) Reverse a list.

# Examples
x = ['a','s','d','f','g']
print x

# We need to find the length to know the number of elements in the list.
a = x[::-1]

print "The List in reverse order looks like: "
print a

# another logic
def reverse(lst):
    i = 0            # first item
    j = len(lst)-1   # last item
    while i<j:
        lst[i],lst[j] = lst[j],lst[i]
        i += 1
        j -= 1
    return lst

print "List reversed again: "
a1=reverse(a)
print a1


# Output.

# ['a', 's', 'd', 'f', 'g']
# The List in reverse order looks like: 
# ['g', 'f', 'd', 's', 'a']
# List reversed again: 
# ['a', 's', 'd', 'f', 'g']

