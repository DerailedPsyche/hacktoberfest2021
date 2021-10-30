#function that takes last element as pivot and places all elements smaller than pivot element to left of pivot and elements
#larger than pvot element to right of pivot
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        if arr[j] <= pivot:
 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
#Quick Sort function
def quicksort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        pi = partition(arr, low, high)
 
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)
 
 
#main program to test code
arr = [5,8,3,4,1,2]
n = len(arr)
quicksort(arr, 0, n-1)
print("Sorted array:")
for i in range(n):
    print(arr[i]),
