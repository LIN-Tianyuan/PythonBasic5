price_str = input("Veuillez entrer le prix des pommes: ")
weight_str = input("Veuillez entrer le poids des pommes: ")
money_int = int(weight_str) * int(price_str)
print("Vous devez payer " + str(money_int) + " euros.")
