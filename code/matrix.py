def convert_to_square_and_sum_diagonal(m, n, elements):
    # Determine size of the square matrix
    max_dim = max(m, n)
    square_matrix = [[1] * max_dim for _ in range(max_dim)]

    # Fill the square matrix with input elements
    index = 0
    for i in range(m):
        for j in range(n):
            square_matrix[i][j] = elements[index]
            index += 1

    # Print original and converted matrix
    print("Original Matrix:")
    for i in range(m):
        print(" ".join(map(str, elements[i * n:(i + 1) * n])))

    print("\nConverted Square Matrix:")
    for row in square_matrix:
        print(" ".join(map(str, row)))

    # Left diagonal elements
    left_diagonal = [square_matrix[i][i] for i in range(max_dim)]
    print("\nLeft Diagonal Elements:", " ".join(map(str, left_diagonal)))

    # Count occurrences of elements
    element_count = {}
    for row in square_matrix:
        for elem in row:
            element_count[elem] = element_count.get(elem, 0) + 1

    print("\nCounting Occurrences in the Matrix:")
    for elem, count in element_count.items():
        print(f"{elem} appears {count} times.")

    # Find non-repeated diagonal elements
    non_repeated = [elem for elem in left_diagonal if element_count[elem] == 1]
    print("\nNon-Repeated Diagonal Elements:", " and ".join(map(str, non_repeated)) if non_repeated else "None")

    # Sum of non-repeated diagonal elements
    print("\nSum of Non-Repeated Diagonal Elements:", sum(non_repeated) if non_repeated else 0)

# Input reading
m, n = map(int, input("Enter dimensions (m n): ").split())
elements = list(map(int, input(f"Enter {m * n} elements: ").split()))
convert_to_square_and_sum_diagonal(m, n, elements)