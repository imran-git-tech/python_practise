#to find the prime number 

number = int(input("enter the number:"))
is_prime = True 

for i in range (2, int(number**0.5)+1):
   if number %i==0:
    is_prime = False
    break

if is_prime and number >1:
  print(number, "it is a prime number")
else:
  print(number, "not a prime")