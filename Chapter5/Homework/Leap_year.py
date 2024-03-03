year = int(input("Veuillez entrer une année: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 100 == 0):
    print(str(year) + " est une année bissextile.")
else:
    print(str(year) + " n'est pas une année bissextile.")