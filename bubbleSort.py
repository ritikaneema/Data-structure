
#bubbleSort
def bubbleSort(arr):
    n=len(arr)#lenght of array
    for i in range(n):#for all array elements :value of i denote no of sorted arr
        for j in range(0,n-1-i):# last i element already in place
            if arr[j]>arr[j+1]:# check element with the next in the arr
                arr[j],arr[j+1]=arr[j+1],arr[j]# swapping if the element is greater thean other element


arr =[2,7,4,1,5,3]
bubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):# loop is for print sorted array
    print("%d" %arr[i]) 
    
