# Création d'une liste
leisure = ['swim', 'dance', 'sing']
print(leisure)
print('------------------------------')
# Longueur d'une liste
print(len(leisure))
print('------------------------------')
# Test de présence d'un élément
print('basketball' in leisure)
print('dance' in leisure)
print('DANCE' in leisure)
print('------------------------------')
# Index d'un élément
print(leisure.index('swim'))
print('------------------------------')
# Accéder aux éléments d'une liste
print(leisure[1])
print('------------------------------')
# Modifier la valeur d'un élément de liste
leisure[0] = 'ski'
print(leisure)
print('------------------------------')
# Ajouter un élément à une liste
leisure.append('game')
print(leisure)
print('------------------------------')
# Insérer un élément ailleurs qu'à la fin
leisure.insert(3, 'climb')
print(leisure)
print(leisure.index('game'))
print(leisure[4])
print('------------------------------')
# Enlever un élément de liste
leisure.remove('climb')
print(leisure)
print('------------------------------')
# Enlever un élément ailleurs avec son index
leisure.pop(1)
print(leisure)
print('------------------------------')
# Vider une liste
leisure.clear()
print(leisure)