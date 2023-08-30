# Input: Number of terms
n = int(input("Enter the number of terms: "))

# Initialize the first two terms
fibonacci_sequence = [0, 1]

# Generate the Fibonacci sequence
while len(fibonacci_sequence) < n:
    next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_term)

# Print the Fibonacci sequence
print("Fibonacci sequence:", fibonacci_sequence)
