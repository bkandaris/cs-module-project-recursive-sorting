# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    merged_arr = arrA + arrB

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        # Determine where the middle of the array is, assign it to a variable
        mid = len(arr) // 2 
        # Split the array into two halves
        L = arr[:mid]  
        R = arr[mid:]
        # use recursion to sort the left/right arrays
        merge_sort(L)
        merge_sort(R)  
        # assign variables to use as a way to hit the base case
        i = 0
        j = 0
        k = 0 
        # Use our counters to reach the 'base case' / reassign arr elements one by one
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # If there is a leftover on the right or left array
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

