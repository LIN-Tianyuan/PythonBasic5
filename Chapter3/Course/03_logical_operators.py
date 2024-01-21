"""
# and
age = int(input("Veuillez entrer votre âge: "))
if age >= 0 and age <= 120:
    print("Âge correct.")
else:
    print("Âge incorrect.")

# or
python_score = int(input("Veuillez entrer votre score Python："))
c_score = int(input("Veuillez entrer votre score C："))
if python_score > 60 or c_score > 60:
    print("Réussir l'examen.")
else:
    print("Continuez à faire du bon travail.")
"""
# not
is_employee = False
if not is_employee:
    print("Veuillez ne pas entrer!")