def multiplyofsumarr(n):
	n=len(arr)
	mid=n//2
	new_arr=[]

	t1=0
	for i in range(0,mid):
		t1=t1+arr[i]
	new_arr.append(t1)

	t2=0
	for j in range(mid,n):
		t2=t2+arr[j]
	new_arr.append(t2)

	print(new_arr)
	print(t1*t2)
arr=[]
soizeofarray=int(input("enter the size of array = "))
for z in range(soizeofarray):
	val=int(input("enter the value = "))
	arr.append(val)
multiplyofsumarr(arr)

