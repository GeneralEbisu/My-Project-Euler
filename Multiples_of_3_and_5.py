from operator import add
from functools import reduce

##############################################################################################
"""Multiples of 3 and 5"""

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
# Take/Learn what you need @ the particular moment.

def main_func(N): # Int -> Int
	assert N > 5
	# Step 1: List all the multiples of 3 & 5 below N.
	L = [i for i in list_multiples_m(3,N)]+[j for j in list_multiples_m(5,N)]
	l = list(set(L))
	# Step 2: Take the sum of this list.
	return reduce(add, l)
#


def list_multiples_m(m, N):
	LN = range(1,N)
	return (x for x in LN if x%m==0)
#


##############################################################################################
def test_run():
	# N = 1000 # 233168
	for N in range(6,100):
		print( main_func(N) )
#


if __name__ == '__main__':
	test_run()
#







