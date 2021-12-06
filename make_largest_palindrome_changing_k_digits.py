# Returns maximum possible
# palindrome using k changes
def maximumPalinUsingKChanges(strr, k):
	palin = strr[::]

	# Iinitialize l and r by leftmost and
	# rightmost ends
	l = 0
	r = len(strr) - 1

	# first try to make palindrome
	while (l <= r):

		# Replace left and right character by
		# maximum of both
		if (strr[l] != strr[r]):
			palin[l] = palin[r] = max(strr[l], strr[r])

			# print(strr[l],strr[r])
			k -= 1
		l += 1
		r -= 1

	# If k is negative then we can't make
	# palindrome
	if (k < 0):
		return "Not possible"

	l = 0
	r = len(strr) - 1

	while (l <= r):

		# At mid character, if K>0 then change
		# it to 9
		if (l == r):
			if (k > 0):
				palin[l] = '9'

		# If character at lth (same as rth) is
		# less than 9
		if (palin[l] < '9'):

			# If none of them is changed in the
			# previous loop then subtract 2 from K
			# and convert both to 9
			if (k >= 2 and palin[l] == strr[l] and
						palin[r] == strr[r]):
				k -= 2
				palin[l] = palin[r] = '9'

			# If one of them is changed in the previous
			# loop then subtract 1 from K (1 more is
			# subtracted already) and make them 9
			elif (k >= 1 and (palin[l] != strr[l] or
							palin[r] != strr[r])):
				k -= 1
				palin[l] = palin[r] = '9'

		l += 1
		r -= 1

	return palin


# Driver code
st = "43435"
st = "535434"
strr = list(st)
k = 2
a = maximumPalinUsingKChanges(strr, k)
print("".join(a))

