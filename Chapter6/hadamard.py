import numpy as np

def hadamard_transform(x, d):
    # Base case: If d == 0, return x as is
    if d == 0:
        return x
    
    # Split the input vector into two halves
    half = len(x) // 2
    x1 = x[:half]
    x2 = x[half:]
    
    # Recursively compute the Hadamard transform on the combined vectors
    y1 = hadamard_transform(x1 + x2, d-1)
    y2 = hadamard_transform(x1 - x2, d-1)
    
    # Combine the results
    return np.concatenate([y1, y2])

# Example usage
d = 2  # depth of the recursion (equivalently, size of the matrix 2^d)
#x = np.random.randn(2**d)  # random input vector of size 2^d
x = np.array([1, 2, 3, 4])
# Compute the result using the recursive Hadamard-like transform
y = hadamard_transform(x, d)

# Print result
print("Input vector:", x)
print("Transformed vector:", y)
