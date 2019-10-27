def linear_search(arr):
    lst = []
    for i in arr:
        if arr.count(i)>1:
            return 'The duplicate element is',arr.count(i)
#print(linear_search([1 , 2, 3, 4, 2]))

#************************#

def binary_search(arr,x):
    start = 0
    end = len(arr)-1

    while start<=end:
        mid = (start+end)//2
        if x == arr[mid]:
            return mid
        elif x>arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False
#print(binary_search([2,3,5,7,9],7))

#************************#

def binary_search_recurr(arr,x,start,end):
    
    if end>= start:
        mid = (start+end)//2
        if x == arr[mid]:
            return mid
        elif x>arr[mid]:
            return binary_search_recurr(arr,x,mid+1,end)
        else:
            return binary_search_recurr(arr,x,start,mid -1)
        
    else:
        return False
    
arr = [2,3,5,7,9]
#print(binary_search_recurr(arr,7,0,len(arr)-1))

#************************#

def binary_search_recursive_modified(arr,x,start,end):
    if end>= start:
        mid = (start+end)//2
        if x == arr[mid]:
            return mid
        elif x>arr[mid]:
            return binary_search_recursive_modified(arr,x,mid+1,end)
        else:
            return binary_search_recursive_modified(arr,x,start,mid -1)
        
    else:
        mid = (start+end)//2
        if x>mid:
            arr.insert(mid+1,x)
            return mid+1
        else:
            arr.insert(mid-1,x)
            return mid-1
#print(binary_search_recursive_modified([0,1,2,8,13,17,19,32,42],3,0,8))


def find_pair(arr,n):
    arr = sorted(arr)
    i=0
    j=1
    while i<len(arr) and j<len(arr):
        if arr[j]-arr[i] == n:
            return (arr[i],arr[j])
        elif n>arr[j]-arr[i]: #diff is greater so increase value
                   j = j + 1
        else: #diff is small so dec val
                   i = i + 1
    return False
arr = [1, 8, 30, 40, 100] 
n = 60
print(find_pair(arr, n))
