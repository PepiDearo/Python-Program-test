print("Allo, quel est votre prenom?")
prenom = input()
print('Nom de famille?')
nomDeFamille = input()
print('Taux horaire?')
tauxHoraire = float(input())
print('Le nombre d\'heures travailles?')
nombreDheureTravailles = int(input())
salaire = tauxHoraire*nombreDheureTravailles

print('Quel est le taux d\'imposition?, ce nombre doit etre entre 0 et 1')
tauxImpo = float(input())
salaireNet = salaire*(1-tauxImpo)

list = ['a','e','i','o','u']
for vowel in list:
    if(prenom[0].casefold() == vowel): #pour les voyelles
        print('Voici le salaire net d\'' + prenom + ': ' + str(salaireNet))
        break
    else: #pour les consonnes
        print('Voici le salaire net de ' + prenom + ': ' + str(salaireNet))
        break



