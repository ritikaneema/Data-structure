#insertion sort
def insertionSort(arr):
	n=len(arr)
	for i in range(1,n): 
		value=arr[i]
		hole=i-1 # i, hole , value comapre thes three
		while hole>=0 and value < arr[hole]:  
			arr[hole+1] =arr[hole]
			hole-=1
                arr[hole+1] = value

arr=[7,2,4,1,5,3]
insertionSort(arr)
for i in range (len(arr)): #loop for print array elements 
    print("%d" %arr[i])
