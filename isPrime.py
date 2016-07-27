#-*-coding:utf8

import math

# num is prime
def isPrime(num):
	"""
	:type num: int
	:rtype: bool
	"""
	for x in xrange(2,int(math.sqrt(num)) + 1):
		if num % x == 0:
			return 1
	return 0
