
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

# from start_num to end_num, the number of prime
def primeNum(start_num,end_num):
	"""
	:type start_num: int
	:type end_num: int
	:rtype: int
	"""	
	sum_num = 0
	for num in xrange(start_num, end_num + 1):
		if isPrime(num) == 1:
			sum_num += 1
	return sum_num
