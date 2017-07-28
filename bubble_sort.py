alist = [54,26,93,17,77,31,44,55,20]

def  bubble_sort(alist):
	for a in range(len(alist)):
		for b in range(len(alist)-1):
			if alist[b] > alist[a]:
				alist[a], alist[b] = alist[b], alist[a]
	print(alist)

bubble_sort(alist)
		