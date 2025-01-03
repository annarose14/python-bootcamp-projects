# Function to add two complex numbers
def add_complex(n1, n2):
    real = n1[0] + n2[0]  # Sum of real parts
    imag = n1[1] + n2[1]  # Sum of imaginary parts
    return (real, imag)

# Input: Real and imaginary parts of two complex numbers
print("For 1st complex number:")
real1 = float(input("Enter the real part: "))
imag1 = float(input("Enter the imaginary part: "))

print("\nFor 2nd complex number:")
real2 = float(input("Enter the real part: "))
imag2 = float(input("Enter the imaginary part: "))

# Add the complex numbers
result = add_complex((real1, imag1), (real2, imag2))

# Print the sum of the complex numbers
print(f"Sum = {result[0]} + {result[1]}i")

