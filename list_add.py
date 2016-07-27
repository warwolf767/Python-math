
#-*-coding:utf8-*-

# The sum of all list elements
def list_add(list_o):
	"""
	:type list_o: list[int]
	:rtype: int
	"""		
	add_sum = 0
	for x in list_o:
		add_sum += x
	return add_sum
