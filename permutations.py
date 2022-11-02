def minimal_perm_length(symbols, n):
	"""
	Calculate the length of the shortest string that could contain all n-length
	permutations of c symbols (with repetition and ordering).
	"""
	# c^n = # of n-length permutations of c symbols (with repetition and ordering)
	# the first permutation requires n symbols
	# every other permutation needs just 1 extra symbol (if we are efficient)
	return n + len(symbols)**n - 1


def minimal_perm_str(symbols, n):
	"""Create minimal string of all n-length permutations of given symbols."""

	# avoiding edge cases
	assert len(symbols) > 0
	assert n > 0
	symbols = list(dict.fromkeys(symbols))	# no duplicated symbols

	# start with n times the last symbol (e.g. n=3, [A,B,C] => "CCC")
	out = symbols[-1]*n 			# this variable contains the str we will return

	# calculate final length of out
	final = minimal_perm_length(symbols, n)

	# append characters that add new permutations until we are done
	while len(out) < final:
		last = out[-n+1:]			# grab last n-1 symbols from out
		for c in symbols:			# try each symbol in ascending order
			if last+c not in out:	# check if appending c would make a new permutation
				out += c  			# if so, append c
				break				# break for-loop = next while-loop iteration
	
	return out						# return permutations string

# main function for testing
symbols = ['A', 'B', 'C']
print(minimal_perm_str(symbols, 3))
print(minimal_perm_length(symbols, 3))

# # intensive testing
# import string
# for i in range(1,27):
# 	symbols = string.ascii_uppercase[:i]
# 	for j in range(2,5):
# 		print(i,j)
# 		p = minimal_perm_str(symbols, j)
# 		print(len(p))
