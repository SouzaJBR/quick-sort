import random
import time
def pivot_select(array, low, high, method=1):
    #print(low, high)
    
    if method == 1:
        r = high
    elif method == 2:
        r = int(low + (high-low)/2)
    elif method == 3:
        r = random.randint(low, high)
    elif method == 4:

        low = low +1
        r = high
        while(True):
            if  low > high:
                break
            if array[low] >= array[low -1]:
                low = low +1
            else:
                r = low
                break
        
    array[r], array[high] = array[high], array[r]
        
    return array[high]

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = pivot_select(arr, low, high, method=4)     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 


def randomize(arr, level):

    high = len(arr)-1
    num_random = int(high*level)

    for _ in range(0, num_random):
        p1 = random.randint(0, high)
        p2 = random.randint(0, high)

        arr[p1], arr[p2] = arr[p2], arr[p1]

def create_array(size):

    return list(range(1, size+1))


arr = create_array(100000)
#print(arr)
randomize(arr, 0.9)
#print(arr)

n = len(arr)

import datetime
started = datetime.datetime.now()
quickSort(arr,0,n-1)
ended = datetime.datetime.now()
print ("Sorted array was: "  + str(ended - started))

arr2 = list(arr)
arr2.sort()
print(str(arr == arr2))
#print(arr)