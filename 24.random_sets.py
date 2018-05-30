# Question - 1.24 (**) Lotto: Draw N different random numbers from a list.

import random
def rnd_select(N, M):	        
	return random.sample(range(1, M+1), N)

# Example

i = input("Enter the number of samples: ")
j = input("Enter the range of samples: ")

print "Random list looks like: "
print rnd_select(i,j)

# Output:-

# Enter the number of samples: 4
# Enter the range of samples: 5
# Random list looks like: 
# [3, 5, 4, 2]
