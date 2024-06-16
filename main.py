# Entrainement POO PIZZA
#---consigne---exo concernant les filtre
#nom, prix, ingredients, vegetarienne
# 1 - afficher uniquement les pizzas vegetariennes
# 2 - afficher les pizzas non vegetariennes
# 3 - que les pizzas qui ont de la tomate
# 4 - Que les pizzas qui coutent moins de 10 euros
#Demander ingredient utilisateur
#calculer le prix
#demander plusieurs pizzas personnalisees
#Amelioration de la pizza personnalisée de maniere automatique(au ieu de mettre 1,ou 2 sur PizzaPersonnalisee(1),  PizzaPersonnalisee(2))


class Pizza:
    def __init__(self, nom, prix, ingredients, vegetarienne=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne

    def afficher_pizza(self):
        vege = ""
        if self.vegetarienne:
            vege += "VEGETARIENNE"
        print("PIZZA :", self.nom, "", self.prix, "€", vege)
        print("INGREDIENTS :", ", ".join(self.ingredients))


class Personnalisee(Pizza):
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENTS = 1
    AUTOMATIQUE_NUMBER = 0

    def __init__(self):
        Personnalisee.AUTOMATIQUE_NUMBER += 1
        self.numero = Personnalisee.AUTOMATIQUE_NUMBER
        super().__init__(f"Personnalisee : {self.numero} ", 0, [])
        self.demander_ingredient_utilisateur()
        self.calculer_prix()
    
    def afficher_pizza(self):
        super().afficher_pizza()

    def demander_ingredient_utilisateur(self):
        while True:
            ingredient = input("Ajouter des ingredients ou (Enter pour afficher choix) ")
            if ingredient == "":
                break
            self.ingredients.append(ingredient)
        print()

    def calculer_prix(self):
        self.prix = self.PRIX_DE_BASE + self.PRIX_PAR_INGREDIENTS * len(self.ingredients)


pizzas = (
     Pizza("4fromage", 10, ("cantal", "emmental", "chevre")),
     Pizza("peperoni", 13, ("PEPERONI", "tomate", "citron")),
     Pizza("calzone", 8, ("roquette", "tomate", "ananas"), True),
     Pizza("vegan", 9, ("oinion", "tomate", "olive", "roquette"), True),
     Personnalisee(),
     Personnalisee(),
    )

for pizza in pizzas:
    pizza.afficher_pizza()
    print()

#---Trier---- on pouvez le faire aussi a l'interieur de notre class
def tri(e):
    return e.nom
        #e.prix
        #len(e.ingredients)

#liste_pizzas.sort(key=tri) #, reverse=True
#déja ici le sort ne fonctionne pas avec le tuple donc il va falloir changer tuple en liste[]


#for pizza in liste_pizzas:
    #pizza.Afficher()
    #if "tomate" in pizza.ingredients: #si y'a de la tomate à l'interieur des ingredients afficher pizza
        # pizza.Afficher()
    #if pizza.prix < 10:
        #pizza.Afficher()
 # if pizza.vegetarienne: #si la pizza est vegetarienne on l'affiche
        #pizza.Afficher()
 # if not pizza.vegetarienne: #si la pizza n'est pas vegetarienne on l'affiche
        #pizza.Afficher()




