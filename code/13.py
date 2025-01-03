# Function for matrix addition
def add_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    sum_matrix = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
    return sum_matrix

# Function for matrix subtraction
def subtract_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    diff_matrix = [[A[i][j] - B[i][j] for j in range(cols)] for i in range(rows)]
    return diff_matrix

# Function for matrix multiplication
def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Matrix multiplication is only possible if columns of A = rows of B
    if cols_A != rows_B:
        return "Matrix multiplication is not possible."

    # Initialize product matrix with zeros
    product_matrix = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                product_matrix[i][j] += A[i][k] * B[k][j]

    return product_matrix

# Input for first matrix
m, n = map(int, input("Enter the number of rows and columns for the first matrix: ").split())
print(f"Enter the elements of the first matrix ({m}x{n}):")
first_matrix = [list(map(int, input().split())) for _ in range(m)]

# Input for second matrix
print(f"Enter the elements of the second matrix ({m}x{n}):")
second_matrix = [list(map(int, input().split())) for _ in range(m)]

# Display the matrices
print("\nFirst Matrix:")
for row in first_matrix:
    print(row)

print("\nSecond Matrix:")
for row in second_matrix:
    print(row)

# Matrix addition
sum_result = add_matrices(first_matrix, second_matrix)
print("\nMatrix Sum:")
for row in sum_result:
    print(row)

# Matrix subtraction
diff_result = subtract_matrices(first_matrix, second_matrix)
print("\nMatrix Difference (Subtraction):")
for row in diff_result:
    print(row)

# Matrix multiplication (only if possible)
product_result = multiply_matrices(first_matrix, second_matrix)
if isinstance(product_result, str):  # Checking if multiplication is possible
    print("\n" + product_result)
else:
    print("\nMatrix Product:")
    for row in product_result:
        print(row)
