def merge(L1, L2):
	c = []
	i = 0
	j = 0
	for l in range(len(L1)+len(L2)):
		c.append(0)
	for k in range(len(c)):
		if j > len(L2) -1:
			c[k] = L1[i]
			i+=1
		elif i > len(L1) -1:
			c[k] = L2[j]
			j+=1
		elif L1[i] < L2[j]:
			c[k] = L1[i]
			i += 1
		else:
			c[k] = L2[j]
			j+=1
	return c
def mergearray(array):
	ret_var = []
	if len(array) == 1:
		return median(array[0])
	ret_var = merge(array[0], array[1])
	if len(array) == 2:
		return median(ret_var)
	for l in range(2, len(array)):
		ret_var = merge(ret_var, array[l])
	return median(ret_var)
def median(array):
	if len(array)%2 == 0:
		mid = (len(array)-1)//2
		return (array[mid]+array[mid+1])/2
	else:
		mid = (len(array)-1)//2
		return array[mid]
