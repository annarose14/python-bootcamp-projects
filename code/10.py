# Input: Number of elements and the array
n = int(input("Enter the number of elements: "))
arr = []

print(f"Enter {n} elements:")
for _ in range(n):
    arr.append(int(input()))

# Calculate sum
sum_of_elements = 0
for num in arr:
    sum_of_elements += num

# Calculate average/mean
average = sum_of_elements / n

# Calculate median
arr.sort()
if n % 2 == 0:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2
else:
    median = arr[n // 2]

# Output results
print(f"Sum: {sum_of_elements}")
print(f"Average: {average:.2f}")
print(f"Mean: {average:.2f}")
print(f"Median: {median}")
