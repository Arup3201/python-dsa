def merge(arr, low, mid, high):
    n1 = mid-low+1
    n2 = high-mid
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]
    i, j = 0, 0
    k = low
    cnt = 0
    while i<n1 and j<n2:
        if left[i]>right[j]:
            arr[k] = right[j]
            cnt += (n1-i)
            j+=1
        else:
            arr[k] = left[i]
            i+=1
        k+=1
    
    while i<n1:
        arr[k] = left[i]
        i+=1
        k+=1
    
    while j<n2:
        arr[k] = right[j]
        j+=1
        k+=1

    return cnt
    
def merge_sort(arr, low, high):
    cnt = 0
    if low<high:
        mid = low + (high-low)//2
        
        cnt += merge_sort(arr, low, mid)
        cnt += merge_sort(arr, mid+1, high)
        cnt += merge(arr, low, mid, high)
        
    return cnt

def inversionCount(arr):
    # Code Here
    n = len(arr)
    cnt = merge_sort(arr, 0, n-1)
    return cnt

if __name__=="__main__":
    arr = [2, 4, 1, 3, 5]
    print(inversionCount(arr))