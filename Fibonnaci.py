# Here's a simple Python program to print the Fibonacci sequence up to a certain number of terms:
# Examples start with 0 and 1 - 0 1 1 2 3

n = int(input("Enter the number of terms: "))

a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
