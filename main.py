# -*- coding: utf-8 -*-
import datetime

date = datetime.datetime.now()

launch = int(input("Voulez-vous créer une nouvelle facture? (1 pour oui, 0 pour non): "))
sexe = int(input("Est-ce que le client est une femme ou un homme ? (0 pour une femme, 1 pour un homme): "))
nom = input("Nom du/de la client(e): ")
prenom = input("Prenom du/de la client(e): ")
code_client = int(input("Code du/de la client(e): "))

reglement_façon = input("Méthode de payement: ")
numero_facture = input("Entrez le numéro de la facture: ")
livraison_jour = int(input("Jour de livraison: "))
livraison_mois = int(input("Mois de livraison: "))
livraison_annee = int(input("Année de livraison: "))

nbr_article = int(input("Nombre d'article: "))
liste_article = []
liste_article_nom = []
liste_article_prix = []
liste_article_nombre = []

fichier = open("facture.txt", "a")


def facture():
    print("Vous créez une facture pour", prenom, nom)
    print(" ")


num_facture = 0

if launch == 1:
    facture()

ajout = 0
base = 1

print(" ")

while ajout != nbr_article:
    print("--> Produit", base)
    code = int(input("Entrez le code d'article: "))
    nom_produit = input("Entrez le nom du produit: ")
    prix = float(input("Entrez le prix du produit: "))
    nombre = int(input("Entrez la quantité: "))
    print(" ")
    liste_article.append(code)
    liste_article_nom.append(nom_produit)
    liste_article_prix.append(prix)
    liste_article_nombre.append(nombre)
    ajout = ajout + 1
    base = base + 1

if sexe == 0:
    sexe = "Mme."
elif sexe == 1:
    sexe = "M."

print(" ")
print("********************")
print("Garage Nelumbo")
print("39 Avenue de Saint-Etienne")
print(" ")
print("42160 Andrézieux-Bouthéon")
print("garage.nelumbo@gmail.com")
print("07.82.75.35.36")
print("********************")
print(" ")
print("FACTURE")
print(sexe, nom, prenom, "|", date.day, "/", date.month, "/", date.year, "|", date.hour, ":", date.minute, ":",
      date.second)
print("Code client: ", code_client, "|", "Règlement: ", reglement_façon)
print("Numéro de facture: ", numero_facture, "|", "Jour de livraison: ", livraison_jour, "/", livraison_mois, "/",
      livraison_annee)
print(" ")
print("********************")

i = 0

for loop in range(nbr_article):
    print(liste_article[0 + i], "-", liste_article_nombre[0 + i], "x", liste_article_nom[0 + i], "-",
          liste_article_prix[0 + i], "---->", liste_article_nombre[0 + i] * liste_article_prix[0 + i])
    i = i + 1

print("TOTAL:", sum(liste_article_prix) * sum(liste_article_nombre), "€")
print("********************")

fichier = open("facture.txt", "a")

fichier.write("********************\nGarage Nelumbo\n39 Avenue de Saint-Etienne\n\n42160 "
              "Andrézieux-Bouthéon\ngarage.nelumbo@gmail.com\n07.82.75.35.36\n********************\n\nFACTURE\n")
fichier.write(sexe), fichier.write(" "), fichier.write(nom), fichier.write(" "), fichier.write(prenom)
fichier.write(" "), fichier.write("|"), fichier.write(" "), fichier.write(date.day), fichier.write("/")
fichier.write(date.month), fichier.write("/"), fichier.write(date.year), fichier.write(" "), fichier.write("|")
fichier.write(" "), fichier.write(date.hour), fichier.write("/"), fichier.write(date.minute), fichier.write("/")
fichier.write(date.second)

fichier.close()
