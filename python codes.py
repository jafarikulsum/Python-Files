"""num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")"""



"""num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")"""



"""num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")"""


"""string = input("Enter a string: ")
print("First three characters:", string[:3])
print("Last three characters:", string[-3:])"""


"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before swapping: a =", a, "b =", b)
a, b = b, a
print("After swapping: a =", a, "b =", b)"""



"""string = input("Enter a string: ")
print("Lower case:", string.lower())"""


"""string = input("Enter a string: ")
print("Upper case:", string.upper())"""


"""num = 7
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print("factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)"""
