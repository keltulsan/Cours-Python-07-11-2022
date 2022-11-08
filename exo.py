from random import *

# DEBUT

# print("bonjour monde")


r=12000
s=1250
e=10
rh=230

assertionUn = (( (365*3) / (24-(16-8)) ) *(rh) > r) == (e*s<r)
value1 = 15740,625 > 12000 #True
value2 = 12500 < 12000 #False
assertionUn = 15740,625 > 12000 == 12500 < 12000 #False
assertionUn = value1 == value2  #False
assertionUn = True == False  #False


# assertionDeux = (( (365*3) / (4-(12-8)) ) *(rh) > r) == (e*s<r)
# value1 = error> 12000 #False
# value2 = 12500 < 12000 #False
# assertionDeux = error > 12000 == 12500 < 12000 #True
# assertionDeux  = value1 == value2  #True
# assertionDeux  = False == False  #True




def add(x, y):
    """addition x et y"""
    return x+y

def sub(x, y):
    """soustraire x et y"""
    return x-y

def multiply(x, y):
    """multiplier x et y"""
    return x*y

def divid(x, y):
    """diviser x et y"""
    if y==0 :
        return print("C'est pas possible de diviser par 0, c'est pas bien")
    return x/y

def divid2(x, y):
    """diviser x et y"""
    try:
        return x / y
    except:
        return None


def modulo(x, y):
    """modulo x et y"""
    return x%y


def CalculSalaireParSeconde(SalaireHoraire, HeureParJourOuvrable,JourOuvrable):
    """calculer salaire par seconde dans une année """
    #assigner à salaireAnnuel, le nombre d'heure travaillée multiplier par le salaire horaire
    salaireAnnuel = SalaireHoraire * HeureParJourOuvrable * JourOuvrable
    #calculer, puis assigner à secondeParAn, le nombre de seconde dans une année non bisextile
    secondeParAn = 365*24*60*60
    #renvoie le salaireAnnuel par le nombre de secondeParAn
    return salaireAnnuel / secondeParAn


def salaireNet(salaireBrut, coeffitient):
    """salaire net avec coeffitient en pourcentage"""
    #calculer et assigner à coeffRevenuRestant le revenu restant 
    coeffRevenuRestant = (1-coeffitient)/100
    #renvoyer le salaire brut multiplier par le coeffitient 
    return salaireBrut * coeffRevenuRestant


def salaireNet(salaireBrut:int, public:bool):
    #si occuper poste fonction publique, alors renvoyer salaire brut - 15%
    if public :
        return salaireBrut * (1-0.15)
    # sinon travailler dans le secteur privé, alors revoyer salaire brut - 23%
    else :
        return salaireBrut * (1-0.23)


def miniGame(z:str):
    """ Fonction qui permet de savoir si le charactère que le joueur rentre est le même que celui rentré en paramètre"""
    # on definit a avec la valeur de z rentré en paramètre
    a = z
    # on défini d'abord mot comme un str vide
    mot=""
    # fait la boucle tant que notre mot n'est pas égale à a
    while mot != a :
        # le joueur rentre la valeur de mot dans la console
        mot = str(input( "Rentrer un charactère : "))
        # on vérifie que le mot rentré comporte un seul est forcément un seul charactère et autre qu'un espace
        if len(mot)>1 or len(mot)==0:
            # si mot vide ou > à 1 renvoyer 
            return "Tes nul"
        # sinon
        else:
            # si le mot rentré par le joueur est égale à a 
            if mot == a :
                # renvoyer tu as réussi
                return "tu as réussis"


cpt = 0
def miniGameRec(z:str):
    #rappel la var cpt
    global cpt
     # le joueur rentre la valeur de mot dans la console
    mot = str(input( "Rentrer un charactère : "))
    # on vérifie que le mot rentré comporte un seul est forcément un seul charactère et autre qu'un espace
    if len(mot)>1 or len(mot)==0 or mot == " ":
        return "test"
    #compteur de tour
    cpt += 1
    print("Compte tour : " + str(cpt))
    # si le mot rentré par le joueur est égale à z
    if mot == z :
        return
    else:
        #récursivité, relance la fonction
        return miniGameRec(z)


# miniGameRec("z")



# tab = [89,94,77,4,2,10,25]
#pour récupérer la valeur 4 je prends dans tab l'index 3
# print(tab[3])
# tab1 = [1]

def concatenate(str1:str, str2:str):
    """fonction qui concatainte 2 str séparé par une virgule"""
    #renvoyer une chaine de charactère
    return str1 + ',' + str2


def occurence(tab, nb:int):
    #def un compteur pour les occurence
    cpt = 0
    #def str vide
    renvoie = ""
    # tant que cpt <= la longueur du tableau en paramètre
    while cpt <= len(tab)-1:
        #si l'index de la valeur est égale à nb
        if tab[cpt] == nb:
            # si mot pas vide
            if renvoie != "" :
                #concataine renvoie avec l'index de l'occurence
                renvoie = renvoie + ',' + str(cpt)
            else :
                renvoie = str(cpt)
                # incrémente le compteur
        cpt += 1
    # renvoyer les occurence de nb
    return renvoie


tableau = [0,1,1,1,0,1,1,0,1]
print(occurence(tableau, 0))
# FIN 
