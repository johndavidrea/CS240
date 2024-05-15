
def insertionSort(array):

    # If the array has less than two elements sorting isn't needed
    if len(array) < 2:
        return

    # Iterate over the array starting from the second element
    for i in range(1, len(array)):

        # Store the current element as the key to be inserted, store the index for it
        key = array[i]
        index = i - 1

        # If an element is greater than the key, move it one position to the right
        while index >= 0 and key < array[index]:

            # Move the element to the right
            array[index + 1] = array[index]
            index -= 1

        # Now put the key into the correct position
        array[index + 1] = key


# Sort an array
array = [2, 115, 133, 45, 7, 117, 53]
insertionSort(array)
print(array)