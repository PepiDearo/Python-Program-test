print("Allo, quel est votre prenom?")
prenom = input()
print('Nom de famille?')
nomDeFamille = input()
print('Taux horaire?')
tauxHoraire = float(input())
print('Le nombre d\'heures travailles?')
nombreDheureTravailles = int(input())
salaire = tauxHoraire*nombreDheureTravailles
list = ['a','e','i','o','u']
for vowel in list:
    if(prenom[0].casefold() == vowel): #pour les voyelles
        print('Voici le salaire d\'' + prenom + ': ' + str(salaire))
        break
    else: #pour les consonnes
        print('Voici le salaire de ' + prenom + ': ' + str(salaire))
        break



