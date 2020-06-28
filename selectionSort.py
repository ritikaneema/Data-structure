#selectionSort
def selectionSort(arr):
     n=len(arr) #length of array
     for i in range (n):#Main loop
         min_i=i
         for j in range(i+1,n): #i is min then check from i+1
             if arr[min_i]>arr[j]:
                 min_i=j
         arr[i],arr[min_i]=arr[min_i],arr[i] # if min_i is greater than other then swapping

arr=[28,77,85,14,45,43]
selectionSort(arr) #call function

print("Sorted array is:")
for i in range(len(arr)): #print array elements
    print("%d" %arr[i])
