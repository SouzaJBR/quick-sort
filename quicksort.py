import random
import time
import datetime


def pivot_median(low, high, arr):
    return int((low + high)/2)

def pivot_highest(low, high, arr):
    return high

def pivot_random(low, high, arr):
    return random.randint(low, high)

def pivot_raul(low, high, arr):
    low = low +1
    r = high
    while(True):
        if  low > high:
            break
        if arr[low] >= arr[low -1]:
            low = low +1
        else:
            r = low
            break
    
    return r


def pivot_select(array, low, high, method=pivot_highest):
    
    r = method(low, high, array)
    array[r], array[high] = array[high], array[r]
    
    return array[high]

def partition(arr,low,high, pivot_method): 
    i = ( low-1 )         # index of smaller element 
    pivot = pivot_select(arr, low, high, method=pivot_method)     # pivot 
  
    for j in range(low , high): 

        if   arr[j] <= pivot: 
          

            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
 
def quickSort(arr,low,high, pivot_method): 
    if low < high: 
  

        pi = partition(arr,low,high, pivot_method) 
  

        quickSort(arr, low, pi-1, pivot_method) 
        quickSort(arr, pi+1, high, pivot_method) 


def randomize(arr, level):

    high = len(arr)-1
    num_random = int(high*level)

    for _ in range(0, num_random):
        p1 = random.randint(0, high)
        p2 = random.randint(0, high)

        arr[p1], arr[p2] = arr[p2], arr[p1]

def create_array(size):

    return list(range(1, size+1))


def run_test(arrays,random_level, pivot_method):

    timedeltas = []
    array_size = len(arrays[0])

    for i in range(0,10):
        
        array = list(arrays[i])
        started = datetime.datetime.now()
        quickSort(array, 0, array_size - 1, pivot_method)
        ended = datetime.datetime.now()

        arr2 = list(array)
        assert(array == arr2)
        
        timedeltas.append(ended - started)
        
    average_timedelta = sum(timedeltas, datetime.timedelta(0)) / len(timedeltas)

    print("Quicksort ==> Array Size: %d | Random Level: %f | Pivot-Method: %s | Average Time: %s" % (array_size, random_level, pivot_method, average_timedelta))
    
def main():

    for array_size in [10,100,1000,10000, 100000]:
        for random_level in [0.5, 1, 2]:

            arrays = []

            for _ in range(0,10):
                array = create_array(array_size)
                randomize(array, random_level)
                arrays.append(array)

            for pivot_method in [pivot_highest, pivot_median, pivot_random, pivot_raul]:
                run_test(arrays, random_level, pivot_method)

if __name__ == "__main__":
    main()



# arr = create_array(100000)
# #print(arr)

# #print(arr)

# n = len(arr)


# started = datetime.datetime.now()

# ended = datetime.datetime.now()
# print ("Sorted array was: "  + str(ended - started))

# arr2 = list(arr)
# arr2.sort()
# print(str(arr == arr2))
# #print(arr)
# print(PIVOT_CHOICE)