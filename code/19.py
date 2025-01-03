def merge_and_calculate(arr1, arr2):
    # Merge the two arrays
    merged_array = arr1 + arr2
    # Sort the merged array to calculate median
    merged_array.sort()

    # Calculate mean (average of the elements)
    mean = sum(merged_array) / len(merged_array)

    # Calculate median
    n = len(merged_array)
    if n % 2 == 0:
        # If the number of elements is even, take the average of the two middle elements
        median = (merged_array[n//2 - 1] + merged_array[n//2]) / 2
    else:
        # If the number of elements is odd, take the middle element
        median = merged_array[n//2]

    # Round mean and median to nearest integer
    mean = round(mean)
    median = round(median)

    return merged_array, mean, median

# Taking input from the user
arr1 = list(map(int, input("Enter the elements of Array 1 (space-separated): ").split()))
arr2 = list(map(int, input("Enter the elements of Array 2 (space-separated): ").split()))

# Call the function to merge and calculate mean & median
merged_array, mean, median = merge_and_calculate(arr1, arr2)

# Output the results
print(f"Merged Array: {merged_array}")
print(f"Mean: {mean}")
print(f"Median: {median}")
