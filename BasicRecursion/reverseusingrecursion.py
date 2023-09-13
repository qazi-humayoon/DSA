def rev(arr,start,end):
    #Checking until start is < end. it will stop once start become larger than end i.e they would have crossed each other.
    if start < end:
        arr[start],arr[end] = arr[end],arr[start]
        rev(arr,start +1,end-1)
arr = [4,3,2,1]
rev(arr,0,len(arr)-1)
print("The reversed array is :-",arr)


