# Here's a simple Python program to calculate the factorial of a number:

num = int(input("Enter a number: "))
factorial = 1

# Calculate factorial
for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}.")
