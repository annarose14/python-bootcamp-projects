def find_unique_diagonal_sum(m, n, elements):
    print("Input:")
    print("Dimensions (m x n):", m, "x", n)
    print("Elements:", elements)

    # Create the matrix
    matrix = [elements[i * n:(i + 1) * n] for i in range(m)]
    print("\nOriginal Matrix:")
    for row in matrix:
        print(row)

    # Make the matrix square by padding with 1
    size = max(m, n)
    square_matrix = [[1] * size for _ in range(size)]
    for i in range(m):
        for j in range(n):
            square_matrix[i][j] = matrix[i][j]

    print("\nSquare Matrix:")
    for row in square_matrix:
        print(row)

    # Get the left diagonal elements
    diagonal_elements = [square_matrix[i][i] for i in range(size)]
    print("\nLeft Diagonal:", diagonal_elements)

    # Get all other elements in the matrix
    other_elements = [square_matrix[i][j] for i in range(size) for j in range(size) if i != j]
    print("Elements elsewhere in the matrix:", other_elements)

    # Find unique diagonal elements
    unique_diagonal = [ele for ele in diagonal_elements if diagonal_elements.count(ele) == 1 and ele not in other_elements]
    print("Unique diagonal elements:", unique_diagonal)

    # Return the sum of unique diagonal elements
    result = sum(unique_diagonal)
    print("Sum of unique diagonal elements:", result)
    return result


# Input
m, n = map(int, input().split())
elements = list(map(int, input().split()))

# Output
find_unique_diagonal_sum(m, n, elements)
