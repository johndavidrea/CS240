def quicksort(array):
    # If the array is only a single value sorting is not needed
    if len(array) <= 1:
        return array
    # Set a pivot point
    pivot = array[0]
    # Split the array into two, with the numbers lower than the pivot on the left
    left = [x for x in array[1:] if x < pivot]
    right = [x for x in array[1:] if x >= pivot]
    # Return the array which will be sorted recursively
    return quicksort(left) + [pivot] + quicksort(right)

arr = [1, 7, 4, 1, 10, 9, -2]
sorted_arr = quicksort(arr)
print("Sorted Array in Ascending Order:")
print(sorted_arr)