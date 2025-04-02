def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            arr[j+1]=key
# Place key at after the element just smaller than it. arr[j + 1] = key
arr = [9, 8, 6, 7, 1]
print("Unsorted Array:", arr)
insertion_sort(arr)
print('Sorted Array: ', arr)



def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]
# Sort the two halves
        mergeSort(sub_array1)
        mergeSort(sub_array2)

        i=0
        j=0
        k=0
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1
# When all elements are traversed in either arr1 or arr2, # pick up the remaining elements and put in sorted array
        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1
        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1
arr = [10, 9, 2, 4, 6, 13]
mergeSort(arr)
print("The Sorted array using merge sort is",arr)
