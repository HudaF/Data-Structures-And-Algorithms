def insertion(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr

arr=[2,7,1,8,5,3,4,6]
print(insertion(arr))


def selection(arr):
    for i in range(len(arr)):
        mini=arr[i]
        for j in range(i,len(arr)):
            if arr[j]<arr[i]:
                mini=arr[j]
        arr[i],mini=mini,arr[i]
    return arr
print(selection(arr))

def bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble(arr))

def merge(B,C):
    lst=[]
    while len(B)>0 and len(C)>0:
        if B[0]<C[0]:
            lst.append(B.pop(0))
        else:
            lst.append(C.pop(0))
    lst+=B
    lst+=C
    return lst

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    B = merge_sort(arr[:mid])
    C = merge_sort(arr[mid:])
    return merge(B,C)
print(merge_sort(arr))


def partition(arr,left,right):
    pivot=left
    pi=left-1
    for i in range(len(arr)):
        if arr[i]<arr[right]:
            pi+=1
            arr[i],arr[pi]=arr[pi],arr[i]
    arr[pi+1],arr[right]=arr[right],arr[pi+1]
    return pi+1

def quick(arr,left,right):
    if left<right:
        p=partition(arr,left,right)
        quick(arr,left,p-1)
        quick(arr,p+1,right)
    return arr
  
print(quick(arr,0,len(arr)-1))
