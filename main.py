from hashlib import *


#-----------------------------
# Mes fonctions
#-----------------------------


def compare(mot1,mot2):
    n=len(mot1)
    nbr=0
    for i in range (n):
        if(mot1[i]!=mot2[i]):
            nbr+=1
    return nbr 

def double_hash(mot):
    """
    fonction de double hash
    """
    hash1 = sha256(f'{mot}'.encode()).hexdigest()
    hash2 = sha256(f'{hash1}'.encode()).hexdigest()
    return hash2

def nbr_tentative(hash_rech,iter=9):
    for i in range (iter+1):
        essais= sha256(f'{i}'.encode()).hexdigest()
        if (compare(essais,hash_rech) != 0):
            return (i+1,i+2)
        else:
            return None

def hash(list):
    hashlist=[]
    for i in range(len(list)):
        hashlist.append(sha256(f'{list[i]}'.encode()).hexdigest())
    return hashlist


#---------------------------------------------------------------------------

#       EXERCICE 1

#
# Partie A — Calcul de hashs SHA-256 
#

# Question 1.1 — Calcul le SHA-256 des chaînes suivantes et complétez le tableau 

tab=["Bitcoin","bitcoin","Blockchain","blockchain","Abidjan2025"]
tab_hash= []
for i in range(len(tab)):
    tab_hash.append(sha256(f'{tab[i]}'.encode()).hexdigest())

for i in range(len(tab)):
    print(f"{tab[i]} = {tab_hash[i]}")

car_diff = compare(tab_hash[0],tab_hash[1])


# Question 1.2 — Comparez SHA-256("Bitcoin") et SHA-256("bitcoin"). Combien de caractères hexadécimaux

print(f"\n\nNombre de caractere different : {car_diff} /64 soit {100*(car_diff/64)}\n")


# Question 1.3 — Calcul SHA-256(SHA-256("Bitcoin"))

print(f"SHA-256(SHA-256('Bitcoin')) = {double_hash('Bitcoin')}")



#
# Partie B — Propriétés de sécurité
#

# Question 1.4 — Irréversibilité. On vous donne le hash suivant :
hash_donnee = "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"

for i in range(10):
    if(compare(hash_donnee,hash([f'{i}'])[0])==0):
        print(f"{hash_donnee} = {hash([f'{i}'])[0]} avec {i+1} tentative(e) ")


# Question 1.5 — Résistance aux collisions. Existe-t-il deux entrées x ≠ y telles que SHA-256(x) = SHA-256(y) 



#       EXERCICE 2

#   Partie A — Construction manuelle 


# Question 2.1 — Soit un bloc Bitcoin contenant 4 transactions. On dispose des données brutes suivantes 

tab_trans = [
'Alice envoie 0.5 BTC à Bob',
'Bob envoie 0.2 BTC à Carol',
'Carol envoie 0.1 BTC à Dave',
'Dave envoie 0.05 BTC à Alice'
]

# a) Calcul des hashs des feuilles H₁, H₂, H₃, H₄ avec SHA-256 appliqué sur les données brutes de chaque transaction

tab_trans_hash = hash(tab_trans)

print("\n\n")
for i in range(len(tab_trans)):
    print(f"H{i+1} = {tab_trans[i]} = {tab_trans_hash[i]}")

# b) Calcul des hashs des nœuds intermédiaires N₁ et N₂
print("\n\n")
def hash_noeud_inter(list):
    H=[]
    for i in range(0,len(list),2):
        H.append(hash([list[i]+list[i+1]])[0])
        print(f"H{i+1}{i+2} = {hash([list[i]+list[i+1]])[0]}")
    return H

noueds_inter= hash_noeud_inter(tab_trans_hash)


# C) Calcul de Merkle Root = SHA-256(H₁₂ ‖ H₃₄).
print("\n\n")
def MerkleRoot(list):
    print(f"Merkle Root = {hash(list[0]+list[1])[0]}")

MerkleRoot(noueds_inter)




# PARTIE B — Immutabilité et preuve d'inclusion
print(f"")



