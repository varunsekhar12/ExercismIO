def binsearch(item,list):
	beg = 0
	last = len(list)-1
	while(beg <= last):
		mid = (beg+last)/2
		if item == list[mid]:
			return mid
		elif list[mid] < item:
			beg = mid+1
		else:
			last = mid-1
	return;


list = []
n = int(raw_input("Enter number of elements : "))
for i in range(0,n):
	l = int(raw_input())
	list.append(l)
print "The List is : "
print list
item = int(raw_input("Enter the item to be searched for : "))
ret = binsearch(item,list)
print "The Position of Item is : "
print ret
