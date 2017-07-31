
#-*-coding:utf8-*-

__anthor__ = 'ice wolf'

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

# Chinese remainder theorem(CRT)		
def remainderX(list_a, list_m):
    """
    :type list_a: list[int]
    :type list_m: list[int]
    :rtype: int
    """		
    # calculate M
    M = list_muit(list_m)
    # generate M1~Mn
    list_M = []
    for x in list_m:
        list_M.append(M / x)
    # generate t1~tn
    list_t = []
    for i in xrange(0,len(list_m)):
        list_t.append(mod1(list_M[i], list_m[i]))
    # calculate X
    X = 0
    for i in xrange(0,len(list_m)):
        X += list_a[i] * list_t[i] * list_M[i]
        X%=M
    return X
