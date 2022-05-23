import numpy as np
import time
from matplotlib import pyplot as plt
import random
# ---------------------------------------------
# ---------- Merge Function -------------------
def merge(arrayLeft, arrayRight):
    result = []
    i = 0
    j = 0
    while i < len(arrayLeft) and j < len(arrayRight):  # looping until one of two lists is empty
        if arrayLeft[i] < arrayRight[j]:
            result.append(arrayLeft[i])  # Putting the smaller element in the sorted list
            i += 1  # Moving the pointer to the next element
        else:
            result.append(arrayRight[j])
            j += 1
    while i < len(arrayLeft):
        result.append(arrayLeft[i])
        i += 1
    while j < len(arrayRight):
        result.append(arrayRight[j])
        j += 1
    return result
# ---------------------------------------------
# ------------ Merge Sort ---------------------
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2  #integer division to get the middle index
    leftArr=arr[:mid]
    rightArr=arr[mid:]
    leftArr=merge_sort(leftArr)
    rightArr=merge_sort(rightArr)
    return list(merge(leftArr,rightArr))
# ----------------------------------------------
# ------------- Insertion Sort -----------------
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        hole=i
        while hole > 0 and arr[hole-1] > key:
            arr[hole]=arr[hole-1]
            hole-=1
        arr[hole]=key
# -----------------------------------------------
# ------------- Selection Sort ------------------
def selection_sort(arr):
    for i in range(len(arr)-1):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min=j
        if i!=min:
            arr[i], arr[min] = arr[min], arr[i]
# ------------------------------------------------
# -------------- Quick Sort ----------------------
# Partition :
def partition(arr, start, stop):
    randpivot = random.randrange(start, stop)
    arr[stop], arr[randpivot] = arr[randpivot], arr[stop]
    x = arr[stop]
    i = start
    for j in range(start, stop):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[stop] = arr[stop], arr[i]
    return i
# Sort :
def quicksort(arr, start, stop):
    if (start < stop):
        pivotindex = partition(arr, start, stop)
        quicksort(arr, start, pivotindex - 1)
        quicksort(arr, pivotindex + 1, stop)
# ----------------------------------------------
# ------------- Hybrid Sort --------------------
def hybrid_sort(arr,t):
    n=len(arr)
    if n == 1:
        return arr
    elif n <= t:
        selection_sort(arr)
        return arr
    else:
        mid=len(arr)//2
        leftArr=arr[:mid]
        rightArr=arr[mid:]
        leftArr=hybrid_sort(leftArr,t)
        rightArr=hybrid_sort(rightArr,t)
        return list(merge(leftArr,rightArr))
# ------------------------------------------------
# ---------- Kth Smallest Element ----------------
def kthSmallest(arr, start, stop, k):
    if 0 < k <= stop - start + 1:
        if start == stop:
            return arr[start]
        pivot = partition(arr, start, stop)
        if pivot - start == k - 1:
            return arr[pivot]
        if pivot - start > k - 1:
            return kthSmallest(arr, start, pivot - 1, k)
        return kthSmallest(arr, pivot + 1, stop, k - pivot + start - 1)
# -------------------------------------------------


if __name__ == "__main__":
    sizes = []
    mergeTimes = []
    selectionTimes = []
    insertionTimes = []
    quickTimes = []

    resume = True
    while resume:
        size = int(input("Enter size of array "))
        sizes.append(size)
        arr = np.random.randint(1, 100, size)
        arr1 = arr
        smerge = time.time()
        merge_sort(arr1)
        emerge = time.time()
        tmerge = (emerge - smerge) * 1000
        mergeTimes.append(tmerge)
        print(f"Merge sort time = {tmerge}ms\n")
        arr2 = arr
        sinsertion = time.time()
        insertion_sort(arr2)
        einsertion = time.time()
        tinsertion = (einsertion - sinsertion) * 1000
        insertionTimes.append(tinsertion)
        print(f"insertion sort time = {tinsertion}ms\n")
        arr3 = arr
        sselection = time.time()
        selection_sort(arr3)
        eselection = time.time()
        tselection = (eselection - sselection) * 1000
        selectionTimes.append(tselection)
        print(f"selection sort time = {tselection}ms\n")
        arr4 = arr
        squick = time.time()
        quicksort(arr4, 0, len(arr4) - 1)
        equick = time.time()
        tquick = (equick - squick) * 1000
        quickTimes.append(tquick)
        print(f"quick sort time = {tquick}ms\n")
        r = input(("If you want to enter another size, enter y "))
        if r != 'y':
            resume = False
    plt.plot(sizes, mergeTimes, marker='o')
    plt.plot(sizes, insertionTimes, marker='o')
    plt.plot(sizes, selectionTimes, marker='o')
    plt.plot(sizes, quickTimes, marker='o')
    plt.xlabel('Size')
    plt.ylabel('Execution Time')
    plt.legend(['Merge', 'Insertion', 'Selection', 'Quick'])
    plt.show()
    sizes.clear()
    mergeTimes.clear()
    insertionTimes.clear()
    selectionTimes.clear()
    quickTimes.clear()
        