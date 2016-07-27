
#-*-coding:utf8-*-

import math

# the factor list of num
def factorList(num):
	"""
	:type num: int
	:rtype: list[int]
	"""		
	factor_list = []
	for n in xrange(2, int(math.sqrt(num)) + 1):
		while num % n == 0:
			factor_list.append(n)
			num = num / n
	if factor_list == []:
		factor_list.append(1)
	if not num == 1: 
		factor_list.append(num)	
	return factor_list
