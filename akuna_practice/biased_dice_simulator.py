#!/usr/bin/env/python3

from functools import lru_cache

"""
A die simulator selectes a random number from 1 to 6 for each roll. The programmer introduced a constraint in the generator: 
it cannot roll the number i more than rollMax[i] times consecutively, where 1 <= i <= 6. Determine the number of distinct sequences 
that may be rolled in some number of rolls, N. A sequence is distinct if there is at least one element that differs when compared to all other sequences. 
The number might be quite large, so return the value modulo 1000000007, (10^9 + 7)

Example:
N = 2
rollMax = [1,2,1,2,1,2]

Looking at rollMax, using 1-based indexing, there can be 1 roll of 1, 2 consecutive rolls of 2, 1 roll of 3, 2 consecutive rolls of 4 and so on.

There will be 2 rolls of the die. For the first roll, there are six possible outcomes, 1 through 6. Lokking at rollMax, there are three values 
that cannot be rolled in consecutive throws, values 1, 3, 5. If there are no constraints on the die, there are 6 possible outcomes in each roll, 
so 6 * 6 = 36 possible combinations. It is known that the sequences (1,1), (3,3) and (5,5) cannot occur, so the final answer is 36 - 3 = 33, 
and 33 mod 1000000007 = 33.

Function Description
Complete the function countDiceSequences in the editor below. The function must return the number of different possible sequences, modulo (10^9 + 7)

countDiceSequences has the following parameters:
	N: The number of times to roll the die
	rollMax: An array of 6 integers, each rollMax[i] denotes the maximum number of consecutive rolls of number i where 1 <= i <= 6.
"""
def countDiceSequences(N: int, rollMax: list) -> int:
	rollMax = [0] + rollMax

	@lru_cache(maxsize= None)
	def helper(n, last= 0):
		if n == 0: return 1
		return sum(helper(n - d, last= i) for i in range(1, 7) if i != last
										for d in range(1, min(n, rollMax[i]+1))) % int(1e9 + 7)

	return helper(N) % int(1e9+7)




if __name__ == '__main__':
	#example 1
	N = 2
	rollMax = [1, 2, 1, 2, 1, 2]

	print(countDiceSequences(N, rollMax))
