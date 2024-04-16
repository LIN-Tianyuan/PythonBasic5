"""
def greet():
    print("Salut, Terrien!")
"""


def greet(firstname, lastname):
    print("Bonjour, " + firstname + " " + lastname + ".")


def season_pref(season="Eté"):
    print("Ma saison préférée : " + season)


def visit(*countries):
    print(countries)


def list_game(competitor_1, competitor_2, competitor_3):
    print("Concurrents du jour: " + competitor_1 + " " + competitor_2 + " " + competitor_3)


# greet("Michael", "Liang")
# greet("Lucas", "Yang")
# season_pref("Printemps")
# season_pref()
# visit("Venezuela", "Allemagne", "Finlande", "France")
# visit("Etat-Unis")
# list_game("Julien", "Anne", "Eva")
list_game("Anne", "Julien", "Eva")
list_game(competitor_2="Julien", competitor_1="Anne", competitor_3="Eva")