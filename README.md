Task-2: Fibonacci Sequence Generator

Question: Create a program that generates the Fibonacci sequence up to a given number of terms.

Code:

n = int(input("Enter the number of terms: "))
fibonacci_sequence = [0, 1]
while len(fibonacci_sequence) < n:
    next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_term)
print("Fibonacci sequence:", fibonacci_sequence)

Logic:
1. The program asks the user to enter the number of terms for input.
2. Start sequence with 0 and 1.
3. Program then adds new terms by taking the sum of the previous two.
4. Repeat till sequence reaches desired number of terms.
5. Print the sequence.

