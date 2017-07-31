
#-*-coding:utf8-*-

__anthor__ = 'ice wolf'

# num * num_r = 1 mod mod_num
def mod1(num, mod_num):
	"""
	:type num: int
	:type mod_num: int
	:rtype: int
	"""		
	i = 1
	while True:
		if((mod_num * i + 1) % num == 0):
			num_r = (mod_num * i + 1) / num
			break
		i = i + 1
	return num_r
