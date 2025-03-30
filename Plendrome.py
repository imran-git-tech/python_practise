# Here's a simple Python program to check if a number is a palindrome:


num = input("Enter a number: ")

# Check if the number is the same forwards and backwards
if num == num[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")


"""""
xample Input and Output:
Input: madam

Output: 'madam' is a palindrome.

Input: 12321

Output: '12321' is a palindrome.

Input: hello

Output: 'hello' is not a palindrome. 

"""   
