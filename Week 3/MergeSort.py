# Mergesort works by splitting a list into two parts, sorting them independantly, and then merging them together
# Define the function, taking in an array as a parameter
def mergeSort(mainArray):
    # If the array only has one value it doesn't need to be sorted
    if len(mainArray) > 1:
        # Use floor division to find midpoint
        midpoint = len(mainArray) // 2

        # Split the array into two halves
        leftArray = mainArray[:midpoint]
        rightArray = mainArray[midpoint:]

        # Call the function recursively to sort the left and right arrays independently
        mergeSort(leftArray)
        mergeSort(rightArray)

        # Declare index variables for the left, right, and main arrays
        indexL = 0
        indexR = 0
        indexM = 0

        # Merge while both the left and right arrays have elements remaining
        while indexL < len(leftArray) and indexR < len(rightArray):
            # Iterate through the left and right arrays, moving values back to the main array as appropriate
            # Compare the values of the two subarrays, check if the left value is <= to the right value
            # If you change the comparison from <= to > it will sort the array in decending order instead
            if leftArray[indexL] <= rightArray[indexR]:
                # If so, set the main array at current index equal to the left value
                mainArray[indexM] = leftArray[indexL]
                # Increment the left index counter
                indexL += 1
            else:
                # If not, set the main array at curret index equal to the right value
                mainArray[indexM] = rightArray[indexR]
                # Increment the right index counter
                indexR += 1
            # Increment the main index after each loop
            indexM += 1

        # Merge when only the left array has elements remaining
        while indexL < len(leftArray):
            # Set the main array at current index equal to the left array at the left index
            mainArray[indexM] = leftArray[indexL]
            # Increment both indices
            indexL += 1
            indexM += 1

        # Merge when only the right array has elements remaining
        while indexR < len(rightArray):
            # Set the main array at current index equal to the right array at the right index
            mainArray[indexM] = rightArray[indexR]
            # Increment both indices
            indexR += 1
            indexM += 1

# Make test array to verify the sorting works properly
testArray = [5, 18, 27, 1, 0, 47, 22, 69]
print(testArray)
mergeSort(testArray)
print(testArray)