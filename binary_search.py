alist = [1,2,3,4,5,6,7]

def bin_search(alist, num):
	
	start = 0
	end = len(alist) - 1
	disc = False


	while start < end and disc == False:
		mid = (start + end)//2
		if alist[mid] == num:
			print("The number is ", num)
			disc = True
		else:
			if num < alist[mid]:
				end = mid - 1
			else:
				start = mid + 1
	

bin_search(alist, 3)