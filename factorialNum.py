# This snippet is to find factorial of a positive integer number.
n = int(input('Enter a positive integer number: '))
factorial = 1
if n < 0:
    print('Factorial of a negative number is not possible.')
elif n == 0:
    print('Factorial of 0 is 1.')
else:
    for i in range(1, n+1):
        factorial = factorial * i
    print('The factorial of ', n, ' is ', factorial)
