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
print('------------------------------')
# Concaténer deux listes
month = ['Janvier', 'Février', 'Mars']
season = ['Automne', 'Hiver', 'Printemps', 'Eté']
various_times = month + season
print(various_times)
print('------------------------------')
month.extend(season)
print(month)
print('------------------------------')
# Créer une tranche de liste
rainbow= ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo', 'violet']
print(rainbow)
print(len(rainbow))
print(rainbow[1:4])
print(rainbow[3:])
print(rainbow[:5])
print(rainbow[-5:-2])

