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

# a) Calcul des hashs des feuilles H1, H2, H3, H₄ avec SHA-256 appliqué sur les données brutes de chaque transaction

tab_trans_hash = hash(tab_trans)

dict_feuil = {}

for i in range(len(tab_trans)):
    dict_feuil[f"H{i+1}"] = tab_trans_hash[i]

print("\n\n")
for i,j in dict_feuil.items():
    print(f"{i} = {j}")

# b) Calcul des hashs des nœuds intermédiaires N₁ et N₂
print("\n\n")
def hash_noeud_inter(list):
    H=[]
    for i in range(0,len(list),2):
        H.append(hash([list[i]+list[i+1]])[0])
        print(f"H{i+1}{i+2} = {hash([list[i]+list[i+1]])[0]}")
    return H

noueds_inter= hash_noeud_inter(tab_trans_hash)


# C) Calcul de Merkle Root = SHA-256(H12 ‖ H34).
print("\n\n")
def MerkleRoot(list):
    print(f"Merkle Root = {hash(list[0]+list[1])[0]}")

MerkleRoot(noueds_inter)




# PARTIE B — Immutabilité et preuve d'inclusion
print(f"")

# Question 2.2 — Modification frauduleuse de Tx2
print("Question 2.2 — Modification frauduleuse de Tx2")
print("Tx2 originale : Bob envoie 0.2 BTC à Carol")

tx2_fraude = "Bob envoie 2.0 BTC à Carol"
tx2_hash_fraude = hash([tx2_fraude])[0]

print(f"Tx2 frauduleuse : {tx2_fraude}")
print(f"H2 originale   : {dict_feuil['H2']}")
print(f"H2 frauduleuse : {tx2_hash_fraude}")

# Recalcul des nœuds impactés
print("\nPropagation des changements :")
print("H2 change → H12 change → Merkle Root change")

# Recalcul avec la fraude
tab_trans_fraude = tab_trans.copy()
tab_trans_fraude[1] = tx2_fraude
tab_trans_hash_fraude = hash(tab_trans_fraude)

noueds_inter_fraude = hash_noeud_inter(tab_trans_hash_fraude)
print(f"\nNouveau H12 : {noueds_inter_fraude[0]}")
print(f"Ancien H12 : {noueds_inter[0]}")

# Nouvelle Merkle Root
print(f"\nNouvelle Merkle Root : {hash(noueds_inter_fraude)[0]}")
print(f"Ancienne Merkle Root : {hash(noueds_inter)[0]}")

print("\n► Détection : La Merkle Root est différente → fraude détectée !")


# Question 2.3 — Merkle Proof (vérification de Tx1)
print("\n\nQuestion 2.3 — Merkle Proof pour Tx1")
print("Vérification que Tx1 est bien incluse dans le bloc")

# Preuve minimale pour Tx1
print("\nÉléments nécessaires pour la preuve :")
print("• H1 : calculé localement depuis Tx1")
print("• H2 : fourni par le nœud (frère de H1)")
print("• H34 : fourni par le nœud (oncle du sous-arbre)")

# Vérification étape par étape
print(f"\nVérification :")
print(f"Tx1 : {tab_trans[0]}")
print(f"H1 = {dict_feuil['H1']}")

# Étape 1 : H1 connu
H1_local = dict_feuil['H1']

# Étape 2 : H12 = SHA-256(H1 ‖ H2)
H12_verification = hash([H1_local + dict_feuil['H2']])[0]
print(f"H12 = SHA-256(H1 ‖ H2) = {H12_verification}")

# Étape 3 : Merkle Root = SHA-256(H12 ‖ H34)
root_verification = hash([H12_verification + noueds_inter[1]])[0]
print(f"Merkle Root = SHA-256(H12 ‖ H34) = {root_verification}")

# Vérification finale
root_original = hash(noueds_inter)[0]
print(f"\nRoot attendue : {root_original}")
print(f"Root calculée  : {root_verification}")

if root_verification == root_original:
    print(" Tx1 est bien incluse dans le bloc !")
else:
    print(" Erreur : Tx1 non incluse")

print(f"\n Efficacité : Seulement 2 hashs nécessaires au lieu de 4 transactions")


# Question 2.4 — Nombre impair de transactions
print("\n\nQuestion 2.4 — Gestion d'un nombre impair de transactions")
print("Règle Bitcoin : dupliquer la dernière feuille")

# Simulation avec 3 transactions
tab_trans_3 = tab_trans[:3]  # Tx1, Tx2, Tx3
print(f"\nTransactions (3) :")
for i, tx in enumerate(tab_trans_3):
    print(f"  Tx{i+1} : {tx}")

# Hashs des 3 transactions
tab_trans_hash_3 = hash(tab_trans_3)
print(f"\nHashs des feuilles :")
for i in range(3):
    print(f"  H{i+1} = {tab_trans_hash_3[i]}")

# Duplication de H3
H3_duplique = tab_trans_hash_3[2]
print(f"\nDuplication de H3 : H33 = H3 = {H3_duplique}")

# Calcul des nœuds intermédiaires
print(f"\nCalcul des nœuds intermédiaires :")
H12_3tx = hash([tab_trans_hash_3[0] + tab_trans_hash_3[1]])[0]
H33_3tx = hash([H3_duplique + H3_duplique])[0]

print(f"H12 = SHA-256(H1 ‖ H2) = {H12_3tx}")
print(f"H33 = SHA-256(H3 ‖ H3) = {H33_3tx}")

# Merkle Root pour 3 transactions
root_3tx = hash([H12_3tx + H33_3tx])[0]
print(f"\nMerkle Root (3 tx) = SHA-256(H12 ‖ H33) = {root_3tx}")
print(f"\nStructure de l'arbre avec 3 transactions :")
print(f"        [Merkle Root]")
print(f"           {root_3tx[:20]}...")
print(f"              /      \\")
print(f"         [H₁₂]      [H₃₃]")
print(f"      {H12_3tx[:20]}...  {H33_3tx[:20]}...")
print(f"         /    \\      /      \\")
print(f"      [H₁]  [H₂]  [H₃]  [H₃]")
print(f"         |     |     |     |")
print(f"       (Tx₁) (Tx₂) (Tx₃) (dup)")
print(f"\n► Règle Bitcoin : La dernière feuille est dupliquée pour former une paire")



