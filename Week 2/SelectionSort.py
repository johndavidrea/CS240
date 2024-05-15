def selectionSort(array):

    # Iterate through each element in the array
    for i in range(len(array)):

        # Remember what our minimum index is
        minimumIndex = i

        # Find the minimum element in every iteration, update the minimum index accordingly
        for j in range(i + 1, len(array)):
            if array[j] < array[minimumIndex]:
                minimumIndex = j

        # Swap the two elements to sort the array
        (array[i], array[minimumIndex]) = (array[minimumIndex], array[i])


# Sort an array
array = [2, 115, 133, 45, 7, 117, 53]
selectionSort(array)
print(array)
