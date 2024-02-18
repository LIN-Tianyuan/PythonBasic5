i = 1
while i <= 9:
    j = 0
    while j < i:
        j = j + 1
        print('%d * %d = %d' % (j, i, j * i), end='\t')
    print()##
    i = i + 1