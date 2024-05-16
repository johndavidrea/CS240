def binarySearchRecursive(array, target, lowpoint=0, highpoint=None):
    # If no highpoint is given, set it to the highest index
    if highpoint is None:
        highpoint = len(array) - 1
    # Handle the base case where the target does not exist in the array
    if lowpoint > highpoint:
        return None
    # Calc the midpoint
    midpoint = (lowpoint + highpoint) // 2
    # Check to see if the target has been found
    if array[midpoint] == target:
        return midpoint
    # Check if the target is on the left side of the array
    if array[midpoint] < target:
        return binarySearchRecursive(array, target, midpoint + 1, highpoint)
    # The target must be on the right side of the array if it's not on the left side or midpoint
    return binarySearchRecursive(array, target, lowpoint, midpoint - 1)

