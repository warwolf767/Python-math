
#-*-coding:utf8-*-

__anthor__ = 'ice wolf'

# The product of all list elements
def list_muit(list_o):
	"""
	:type list_o: list[int]
	:rtype: int
	"""		
	muit_sum = 1
	for x in list_o:
		muit_sum *= x
	return muit_sum	
