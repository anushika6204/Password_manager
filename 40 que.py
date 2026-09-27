# check if a number is a palindrome.

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

# Reverse a integer number.

num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse:", reverse)

# check if a number is prime.

num = int(input("Enter a number: "))

if num < 2:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")


#Print Prime Numbers in a Range (use of nested loop)

start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end + 1):

    if num < 2:
        continue

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)

  #Find Factorial of a Number
num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial:", factorial) 

#Generate Fibonacci Series

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c

# Find the Nth Fibonacci Number
n = int(input("Enter n: "))

a = 0
b = 1

for i in range(n):
    a, b = b, a + b

print("Nth Fibonacci number:", a)

#Check if a Number is Armstrong

num = int(input("Enter a number: "))

original = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10

if sum == original:
    print("Armstrong")
else:
    print("Not Armstrong")

# another method
num = int(input("Enter a number: "))

original = num
digits = len(str(num)) # when the number of digits is not known
total = 0

while num > 0:
    digit = num % 10
    total += digit ** digits
    num //= 10

if total == original:
    print("Armstrong")
else:
    print("Not Armstrong")

#Check if a Number is Perfect

num = int(input("Enter a number: "))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum = sum + i

if sum == num:
    print("Perfect Number")
else:
    print("Not Perfect Number")







