#selectionSort
def selectionSort(arr):
     n=len(arr)
     for i in range (n):
         min_i=i
         for j in range(i+1,n):
             if arr[min_i]>arr[j]:
                 min_i=j
         arr[i],arr[min_i]=arr[min_i],arr[i]

arr=[28,77,85,14,45,43]
selectionSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" %arr[i])
