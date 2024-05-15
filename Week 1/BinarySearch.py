# Read the file and generate an array
def read_file(filepath):
    number_list = []

    # Open file, use read mode
    with open(filepath, 'r') as file:
        # Append each line to the array
        for line in file:
            number_list.append(int(line.strip()))

    return number_list

def binary_search(numbers, item):
    # Define lower and upper bounds of search
    lowpoint = 0
    highpoint = len(numbers) - 1
    operations = 0

    while lowpoint <= highpoint:
        operations += 1
        # Calculate the middle value between the lower and upper bounds, then guess that
        midpoint = (lowpoint + highpoint) // 2
        guess = numbers[midpoint]

        # Check if the number is lower or higher, adjust lower/upper bound accordingly
        if guess == item:
            return midpoint, operations
        if guess > item:
            highpoint = midpoint - 1
        else:
            lowpoint = midpoint + 1

        # Repeat until number is found

    return None, operations

filepath = "numbers.txt"
numbers_list = read_file(filepath)

target = 51216352  # Example target value for binary search
result_index, operation_count = binary_search(numbers_list, target)
print(f"Index of {target}:", result_index)
print(f"Operations needed to find index:", operation_count)
