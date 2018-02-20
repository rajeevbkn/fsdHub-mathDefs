#This is a programme to add digits of a number and return its sum.
n = int(input('Enter the number: '))
sum = 0
while n > 0:
    remainder = n % 10
    sum = sum + remainder
    n = n // 10 
print('The sum of digits of the number entered by you is:', sum)
