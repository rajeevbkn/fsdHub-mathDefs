# The solution finder of the Pythagorian Theorem.

from math import sqrt


def squarert(x):
    xrt = sqrt(x)
    return xrt


print('The solution finder of the Pythagorian Theorem\n')
print('Let a be the perpendicular, b be the base and c be the hypoteneous of the triangle.\n')
print('a, b & c have non-zero values.\n')

find_side = input('Which side of the triangle do you want to be computed? = ')

if find_side == 'a':
    xp = find_side
    xb = float(input('What is the value of b? = ')) and != 0
    xh = float(input('What is the value of c? = '))
    xp = squarert((xh ** 2 - xb ** 2))
    print('result a = ', '%.1f' % xp, )

elif find_side == 'b':
    xp = float(input('What is the value of a? = '))
    xb = find_side
    xh = float(input('What is the value of c? = '))
    xb = squarert((xh ** 2 - xp ** 2))
    print('result b = ', '%.1f' % xb)

else:
    xp = float(input('What is the value of a? = '))
    xb = float(input('What is the value of b? = '))
    xh = find_side
    xh = squarert((xp ** 2 + xb ** 2))
    print('result c = ', '%.1f' % xh)
