import random
computer = random.randint(1, 100)
count = 0
while True:
    num = int(input("Veuillez entrer un nombre: "))
    count = count + 1
    if num < computer:
        print("Plus petit.")
    elif num > computer:
        print("Plus grande.")
    else:
        print("Félicitation!")
        print("Vous avez bien deviné " + str(count) + " fois au total.")
        break
