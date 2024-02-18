"""
star = '*'
for element in range(9):
    for element in range(9):
        print(star, end='')
    print()
"""

i = 1
while i < 9:
    j = 0
    while j < i:
        print('*', end='')
        j = j + 1
    print()
    i = i + 1



