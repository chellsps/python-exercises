def sel_sort():
	list1 = [2, 5, 3, 9, 65, 1]
	l = len(list1)
	for i in range(1, l-1):
		min1 = i
		for j in range (i+1, l):
			if list1[j] < list1[min1]:
				min1 = j
			if min1 != i:
				swap(list1[min1] and list1[j])
	print(list1)

def swap(alist, x, y):
	temp = alist[x]
	alist[x] = alist[y]
	alist[y] = temp

sel_sort()

