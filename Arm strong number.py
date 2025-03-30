# Here's a simpler version of the Armstrong number program:


num = int(input("Enter a number: "))
sum_of_digits = 0
temp = num
# Find the number of digits
num_digits = len(str(num))

# Calculate the sum of each digit raised to the power of num_digits
while temp > 0:
    digit = temp % 10
    sum_of_digits += digit ** num_digits
    temp //= 10

if sum_of_digits == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


""""
Example:
153 is an Armstrong number because:
1*1*1 + 5*5*5 + 3*3*3 = 153"
"""