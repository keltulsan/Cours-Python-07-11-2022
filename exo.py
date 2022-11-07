DEBUT

print("bonjour monde")


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


assertionDeux = (( (365*3) / (4-(12-8)) ) *(rh) > r) == (e*s<r)
value1 = error> 12000 #False
value2 = 12500 < 12000 #False
assertionDeux = error > 12000 == 12500 < 12000 #True
assertionDeux  = value1 == value2  #True
assertionDeux  = False == False  #True




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
    return x/y

def modulo(x, y):
    """modulo x et y"""
    return x%y

def CalculSalaireParSeconde(SalaireHoraire, HeureParJourOuvrable,HeureParJourOuvrable):
    """calculer salaire par seconde dans une année x et y"""
    return ((((SalaireHoraire*HeureParJourOuvrable*HeureParJourOuvrable)/365)/24)/60)/60

def salaireNet(salaireBrut, coeffitient):
    """salaire net """
    return salaireBrut*(coeffitient/100)

FIN