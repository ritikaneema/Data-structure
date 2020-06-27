#Binary Search
def binSearch(arr,l,r,key):#create function l=left,r=right
    while l<=r: #check this conditon 
        mid=l+(r-1)//2
        if key==arr[mid]: #check if key is eqal to mid index value
            return mid
        elif key<arr[mid]: 
            return binSearch(arr,l,mid-1,key) #elif condition is true then mid index at mid-1
        else:
            return binSearch(arr,mid+1,r,key) #this condition is true then mid index ar mid+1
    
    return -1 #at this index the element was not present
        
    
arr=[3,6,8,12,14,18]
key=14 
result = binSearch(arr,0,len(arr)-1,key) #function calling

if result != -1:
    print("Element is present at index % d" %result )
else:
    print("Element is not present on array")









    
