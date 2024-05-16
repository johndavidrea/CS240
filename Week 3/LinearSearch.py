# Take in an array and target
def iterativeSearch(array, target):
    # Loop through each element of the array
    for index in array:
        # Compare the current element of the array with the target
        if array[index] == target:
            # If a match is found, return the index
            return index
    # If the loop completes without finding the target, then the target does not exist in the array
    return None


# Take in an array and target, optionally take in an index (defaults to 0 if not specified)
def recursiveSearch(array, target, index=0):
    # Check the base case, look to see if the index is greater than or equal to the length of the array
    if index >= len(array):
        # If so the target is not found. Return None.
        return None
    # Check to see if the current index is the target
    if array[index] == target:
        # If so, return the index
        return index
    # Return the recursive function with the index incremented by 1
    return recursiveSearch(array, target, index + 1)
