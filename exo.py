from random import randint 

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

def concatenate(str1:str, str2:str)->str: 
    """fonction qui concatainte 2 str séparé par une virgule"""
    #renvoyer une chaine de charactère qui concataine str1 et str2 séparé par une virgule
    return str1 + ', ' + str2


def occurence(tab:list, nb:int)->str :
    """Fonction qui renvoie l'index des occurences de nb dans tab"""
    #def cpt un compteur pour les occurences en int. Initialiser à 0
    cpt = 0
    #def renvoie un str vide ou sera ensuite incrémenté les occurences de nb dans tab
    renvoie = ""
    # tant que cpt <= la longueur du tableau en paramètre -1 
    while cpt <= len(tab)-1:
        #si l'index de la valeur de tab est égale à nb
        if tab[cpt] == nb:
            # si renvoie n'est pas vide
            if renvoie != "" :
                #concataine renvoie avec l'index de l'occurence cpt qui est transformé en str
                renvoie = renvoie + ', ' + str(cpt)
            else :
                renvoie = str(cpt)
        # incrémente le compteur de 1 à chaque boucle 
        cpt += 1
    # renvoyer les occurence de nb
    return renvoie

print(concatenate("kono", "Dio DA !!!"))
tableau = [0,1,1,1,0,1,1,0,1]
print(occurence(tableau, 0))





#définir une fonction findIndexes qui prend en paramètres un tableau tableau et un nombre x qui renvoie le nombre d'occurence de x dans tableau
def findIndexes(tab, x):
    #initialisation de i à 0 pour débuter un compteur
    i = 0
    #initialisation de chaineRetour comme mot vide pour ensuite être modifié
    chaineRetour = ""
    #initialisation de isFirst à True
    isFirst = True
    #tant que i est inférieur à la longueur de tableau (fonction len(tableau))
    while i < len(tab):
        # alors
        #défini la var selected avec la valeur de tableau à l'index i
        selected = tab[i]
        #si la valeur de selected est égale à la valeur de x 
        if selected == x:
            #alors
            # si isFirst est vrai 
            if isFirst :
                # alors on assigne à chaineRetour la valeur de i
                chaineRetour = chaineRetour + str(i)
                # on assigne à isFirst False
                isFirst = False
            #sinon
            else :
                #on concatainer chaineRetour avec la fonction concatWithComma de paramètre chaineRetour et l'index i
                chaineRetour = concatenate(chaineRetour, str(i))
        #on incrémente i de 1 à chaque fin de boucle
        i += 1
    #renvoyer chaineRetour composée des index des valeurs pour lesquelles x est dans tableau
    return chaineRetour

print(findIndexes(tableau, 0))

#defini la fonction fibonacci qui prend en paramètre un x et une longueurMax
def fibonacci(x:int, longueurMax:int): 
    # initialise suite en tant que liste d'index 0 valant 0 
    suite = [0]
    # initialise isFirst à True
    isFirst = True
    # Pour la valeur de i jusqu'à la longueur de longueurMax
    for i in range(longueurMax):
        # alors
        # si isFirst vaut True
        if isFirst == True :
            # alors 
            # liste suite est incrémenter de la valeur de x
            suite.append(x)
            # assigne à isFirst False
            isFirst = False
        #sinon
        else:
            # alors
            # liste suite est incrémenter la valeur de suite d'index i et la valeur d'index i - 1
            suite.append(suite[i-1] + suite[i])
    #renvoyer suite
    return suite

print(fibonacci(5, 5))


# def conway(x):
#     L = [[]] * x
#     for i in range(x):
#         for j in range(x):
#             L[i][j] = randint(0,1)
#     return L
            
# print(conway(5))   



# FIN 



# DEBUT


# defini une fonction gagnant de paramètres joueur1_coup joueur2_coup
    # initialisation de gagnant valant 0 si gaganant vaut 1 le gagnant est le joueur 1, si gagnant vaut 2 le gagnant est le joueur 2, et si gagnant vaut 0 c'est une égalité
    # si joueur1_coup vaut pierre
        # alors
        # si joueur1_coup vaut pierre
            # alors
            # assigner à gaganant la valeur 0
        # si joueur1_coup vaut papier
            # alors
            # assigner à gaganant la valeur 2
        # si joueur1_coup vaut ciseaux
            # alors
            # assigner à gaganant la valeur 1
    # si joueur1_coup vaut papier
        # alors
        # si joueur1_coup vaut pierre
            # alors
            # assigner à gaganant la valeur 1
        # si joueur1_coup vaut papier
            # alors
            # assigner à gaganant la valeur 0
        # si joueur1_coup vaut ciseaux
            # alors
            # assigner à gaganant la valeur 2
    # si joueur1_coup vaut ciseaux
        # alors
        # si joueur1_coup vaut pierre
            # alors
            # assigner à gaganant la valeur 2
        # si joueur1_coup vaut papier
            # alors
            # assigner à gaganant la valeur 1
        # si joueur1_coup vaut ciseaux
            # alors
            # assigner à gaganant la valeur 0
    # renvoyer gagnant




# defini la fonction pierrePapierCiseau de paramètres multiplayer qui est un booléen , nbRound qui est un int
    # initialisation du speudo du joueur un grâce au retoure l'éxécution de la fonction input de paramètre le nom du joueur
    # initialisation d'un compteur de point nommé pointJoueur1 du joueur à 0
    # initialisation du choix du joueur1 qui est un mot vide nommé choixJoueur1
    # initialisation d'un dictionnaire nommé dico qui a pour clè le nom de la main joué et la valeur de celui-ci {pierre:0, papier:1, ciseaux:2}
    # initialisation de isRègle valant grâce au retoure l'éxécution de la fonction input de paramètre le choix si le joueur veut voir les règles
    # initialisation de règlesDuJeu qui est un str expliquant les règles du jeu
    # si isRègle vaut vrai
        # alors
        # afficher règlesDuJeu grâce au retour de l'éxécution de la fontion print de paramètre règlesDuJeu 

    #Si gameMode est True 
        # alors
        # initialisation du speudo d'un second joueur un grâce au retoure l'éxécution de la fonction input de paramètre le nom du joueur
        # initialisation d'un compteur de point nommé pointJoueur2 du joueur à 0
        # initialisation du choix du joueur2 qui est un mot vide choixJoueur2
        # afficher le choix des coups possibles grâce au retour de l'éxécution de la fontion print de paramètre dico
        # assigner à choixJoueur1 la valeur du retour de l'éxécution de la fonction input de paramètre le numéro de clé du dictionnaire pour choisir le coup qu'il veut jouer
        # assigner à choixJoueur2 la valeur du retour de l'éxécution de la fonction input de paramètre le numéro de clé du dictionnaire pour choisir le coup qu'il veut jouer

    # Sinon 
        # alors
        # initialisation du choix du bot qui est un mot vide 
# FIN
