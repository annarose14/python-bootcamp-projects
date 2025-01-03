# Function to calculate mean and median
def calculate_mean_and_median(arr):
    # Calculate the mean
    total_sum = sum(arr)
    mean = total_sum / len(arr)
    
    # Sort the array
    arr.sort()
    
    # Calculate the median
    n = len(arr)
    if n % 2 == 0:
        median = (arr[n // 2 - 1] + arr[n // 2]) / 2.0  # Average of two middle elements
    else:
        median = arr[n // 2]  # Middle element
    
    # Print results
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")

# Input: Number of elements and array elements
n = int(input("Enter the number of elements: "))
arr = []

print("Enter the elements:")
for _ in range(n):
    arr.append(int(input()))

# Calculate and display mean and median
calculate_mean_and_median(arr)
