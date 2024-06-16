
#nom, prix, ingredients, vegetarienne

#---consigne---exo concernant les filtre
# 1 - afficher uniquement les pizzas vegetariennes
# 2 - afficher les pizzas non vegetariennes
# 3 - que les pizzas qui ont de la tomate
# 4 - Que les pizzas qui coutent moins de 10 euros
#Demander ingredient utilisateur
#calculer le prix
#demander plusieurs pizzas personnalisees
#Amelioration de la pizza personnalisée de maniere automatique(au ieu de mettre 1,ou 2 sur PizzaPersonnalisee(1),  PizzaPersonnalisee(2))

class Pizza:
    def __init__(self, nom, prix, ingredients, vegetarienne = False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne


    def Afficher(self):
        vege_str = ""
        if self.vegetarienne:
            vege_str = "- VEGETARIENNE"
        print(f"PIZZA : {self.nom}: {self.prix}£ " + vege_str)
        print(", ".join(self.ingredients))
        print()


class PizzaPersonnalisee(Pizza):
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2
    dernier_numero = 0

    def __init__(self):     #, numero
        PizzaPersonnalisee.dernier_numero += 1      #incrementer 1    attention pr utiliser la variable de classe il faut bien passer par le nom de la class com PizzaPersonnalisee.dernier_numero. avec le self.dernier_numero ça peut marcher mais pas preferable attention
        self.numero = PizzaPersonnalisee.dernier_numero
        super().__init__(f"Personnalisée {str(self.numero)}", 0, [])  # () parenthése vide pr ingredients . mais attention la suite pr initialiser avec une liste pr pouvoir ajouter les ingredients donc modifier par []
        #self.demander_ingredients_utilisateurs()
        self.calculer_le_prix()

    def demander_ingredients_utilisateurs(self):
        print()
        #"Ingredients pour la pizza personnalisee 1"
        print(f"Ingredients pour la pizza personnalisee {self.numero}")

        while True:
            ingredient = input("Ajouter un ingredient (ou ENTER pour terminer) : ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"vous avez {len(self.ingredients)} ingredient(s) : {', '.join(self.ingredients)} ")


    def calculer_le_prix(self):
        self.prix = self.PRIX_DE_BASE + len(self.ingredients) * self.PRIX_PAR_INGREDIENT


liste_pizzas = [
    Pizza("4 frommage", 8.5, ("brie", "emmental", "compté", "parmésan"), True),
    Pizza("Pepperoni", 9.5, ("Jambon", "pepperoni", "tomate")),
    Pizza("Indienne", 13, ("champignons", "onion", "emmental", "poulet")),
    Pizza("Vegetarienne", 9, ("tomate", "poivrons", "onion", "champignons", "poivrons"), True),
    PizzaPersonnalisee(),
    PizzaPersonnalisee()
    #PizzaPersonnalisee(1),
    #PizzaPersonnalisee(2)
    ]

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


#EXERCICE

"""class Pizza:
    def __init__(self, nom, prix, ingredients, vegetarienne = False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne

    def Afficher(self):
        vege_str = ""
        if self.vegetarienne:
            vege_str += "- VEGETARIENNE"
        print("PIZZA : " + self.nom + " " + str(self.prix) + "£ " + vege_str)
        print("INGREDIENTS : ", ", ".join(self.ingredients))



class PizzaPersonnalisee(Pizza):
    PRIX_DE_INGREDIENTS = 1.2
    PRIX_DE_BASE = 7
    dernier_numero = 0
    def __init__(self):
        PizzaPersonnalisee.dernier_numero += 1
        numero = PizzaPersonnalisee.dernier_numero
        super().__init__(f"Personalisée ({str(numero)}) : ", 0, [])
        #self.demander_pizza_personnalise()
        self.calculer_prix()

    def demander_pizza_personnalise(self):
        print()
        while True:
            ingredient = input("Ajouter un ingredients ou (ENTER pour quitter) ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"vous avez {len(self.ingredients)}- ingredients : {', '.join(self.ingredients)}")


    def calculer_prix(self):
        self.prix = self.PRIX_DE_BASE + len(self.ingredients) * self.PRIX_DE_INGREDIENTS



liste_pizzas = (
                Pizza("4 fromage", 9, ("tomate", "emmmental", "saucisse"), True),
                Pizza("Indienne", 12, ("champignons", "onion", "emmental", "poulet")),
                Pizza("Vegetarienne", 13, ("tomate", "vegan", "champignos","poivrons"), True),
                Pizza("Hawai", 8, ("ananas", "lardon", "onion")),
                PizzaPersonnalisee(),
                PizzaPersonnalisee()
            )
"""


#for pizza in liste_pizzas:
    #pizza.Afficher()
    #print()


#exo

#nom, prix, ingredients, => vegetarienne

#---consigne---exo concernant les filtre
# 1 - afficher uniquement les pizzas vegetariennes
# 2 - afficher les pizzas non vegetariennes
# 3 - que les pizzas qui ont de la tomate
# 4 - Que les pizzas qui coutent moins de 10 euros
#Demander ingredient utilisateur (perdsonnalisée)
#calculer le prix
#demander plusieurs pizzas personnalisees
#Amelioration de la pizza personnalisée de maniere automatique(au ieu de mettre 1,ou 2 sur PizzaPersonnalisee(1),  PizzaPersonnalisee(2))
"""
class Pizza:
    def __init__(self, nom, prix, ingredients, vegetarienne=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne


    def afficher_pizza(self):
        VEGE = " "
        if self.vegetarienne:
            VEGE += "-Vegetarienne"
        print("PIZZA  : ", self.nom + " " + str(self.prix) + " € " + VEGE)
        print("INGREDIENTS : ", ", ".join(self.ingredients))


class PizzaPersonnalisee(Pizza):
    PRIX_PAR_INGREDIENTS = 2
    PRIX_DE_BASE = 8
    nombre = 0

    def __init__(self):
        PizzaPersonnalisee.nombre += 1
        number = PizzaPersonnalisee.nombre
        super().__init__(f"Personnalisée: {str(number)} ", 0, [])
        self.demander_ingredient()
        self.prix_pizza_personnalise()

    def demander_ingredient(self):
        while True:
            ingredients_str = input("Ajouter ingredients ou taper enter pr quitter : ")
            if ingredients_str == "":
                return ingredients_str

            self.ingredients.append(ingredients_str)
            print("vous avez ajouté ", len(self.ingredients), "ingredients")
            print()

    def prix_pizza_personnalise(self):
        self.prix = self.PRIX_DE_BASE + len(self.ingredients) * self.PRIX_PAR_INGREDIENTS



pizza1 = Pizza("4 fromage", 7, ("gradono", "bleu", "emmental", "fourme d'ambert"), True)
pizza2 = Pizza("Indienne", 8, ("champignons", "emmental", "poulet", "oignon"), False)
pizza3 = Pizza("Vegetarienne", 13, ("tomate", "poivron", "olive"), True)



liste_pizza = [
    pizza1, pizza2, pizza3, PizzaPersonnalisee(), PizzaPersonnalisee()
]


def tri(e):
    return e.prix

liste_pizza.sort(key=tri, reverse=False)

for pizza in liste_pizza:
    pizza.afficher_pizza()
    print()"""







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




