# TP1 Blockchain : Fondamentaux de la Blockchain

Projet éducatif complet pour comprendre les concepts fondamentaux de la blockchain à travers des implémentations pratiques en Python.

## 🎯 Objectifs Pédagogiques

Ce projet vise à démontrer les mécanismes essentiels qui sous-tendent la technologie blockchain :

- **Hachage SHA-256** : Comprendre les propriétés des fonctions de hachage cryptographiques
- **Arbres de Merkle** : Appréhender la structure de données pour l'intégrité des transactions
- **Immutabilité** : Découvrir comment la blockchain garantit l'intégrité des données
- **Preuve d'inclusion** : Vérifier l'existence d'une transaction sans révéler tout le bloc

## 🚀 Fonctionnalités Implémentées

### Exercice 1 : Calculs SHA-256 et Propriétés
- ✅ Calcul de hachages SHA-256 pour différentes chaînes de caractères
- ✅ Analyse de la sensibilité à la casse (Bitcoin vs bitcoin)
- ✅ Démonstration du double hachage SHA-256(SHA-256(x))
- ✅ Illustration de l'irréversibilité et de la résistance aux collisions

### Exercice 2 : Arbres de Merkle et Intégrité
- ✅ Construction manuelle d'un arbre de Merkle avec 4 transactions
- ✅ Calcul de la racine de Merkle (Merkle Root)
- ✅ Démonstration de détection de fraude par modification de transaction
- ✅ Implémentation de preuve d'inclusion (Merkle Proof)
- ✅ Gestion des nombres impairs de transactions

## 📋 Prérequis

- Python 3.x
- Aucune dépendance externe (utilise uniquement le module `hashlib` standard)

## 🛠️ Installation et Utilisation

### Cloner le projet
```bash
git clone https://github.com/KAMB02/TP1_Blockchain.git
cd TP1_Blockchain
```

### Exécuter les exercices
```bash
python main.py
```

Le programme exécutera automatiquement tous les exercices et affichera les résultats dans la console.

## 📚 Contenu Détaillé

### Exercice 1 : Fondamentaux du Hachage

#### Partie A - Calculs SHA-256
Calcul des hachages pour :
- `"Bitcoin"` → Hash unique
- `"bitcoin"` → Hash différent (sensibilité à la casse)
- `"Blockchain"` → Hash de la version majuscule
- `"blockchain"` → Hash de la version minuscule
- `"Abidjan2025"` → Hash personnalisé

#### Partie B - Propriétés de Sécurité
- **Irréversibilité** : Démonstration de l'impossibilité de retrouver l'entrée depuis le hash
- **Résistance aux collisions** : Discussion sur la probabilité de trouver deux entrées avec le même hash

### Exercice 2 : Arbres de Merkle

#### Scénario de Transactions
Le projet simule un bloc Bitcoin contenant 4 transactions :
1. Alice envoie 0.5 BTC à Bob
2. Bob envoie 0.2 BTC à Carol  
3. Carol envoie 0.1 BTC à Dave
4. Dave envoie 0.05 BTC à Alice

#### Construction de l'Arbre
```
        [Merkle Root]
           /      \
      [H₁₂]      [H₃₄]
         /    \      /    \
      [H₁]  [H₂]  [H₃]  [H₄]
         |     |     |     |
       (Tx₁) (Tx₂) (Tx₃) (Tx₄)
```

#### Détection de Fraude
Le programme démontre comment une modification frauduleuse (Tx2 : 0.2 BTC → 2.0 BTC) propage des changements à travers l'arbre jusqu'à la racine, rendant la fraude immédiatement détectable.

#### Preuve d'Inclusion
Implémentation d'une Merkle Proof efficace permettant de vérifier l'existence d'une transaction en utilisant seulement 2 hashs au lieu des 4 transactions complètes.

## 🧮 Exemples de Résultats

### Calculs SHA-256
```
Bitcoin = 6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b
bitcoin = b2c3ae1b8c1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1
Nombre de caractères différents : 43/64 soit 67.19%
```

### Arbre de Merkle
```
H1 = [hash de "Alice envoie 0.5 BTC à Bob"]
H2 = [hash de "Bob envoie 0.2 BTC à Carol"]
H3 = [hash de "Carol envoie 0.1 BTC à Dave"]
H4 = [hash de "Dave envoie 0.05 BTC à Alice"]

H12 = SHA-256(H1 ‖ H2)
H34 = SHA-256(H3 ‖ H4)

Merkle Root = SHA-256(H12 ‖ H34)
```

## 🔍 Concepts Clés Démontrés

### Propriétés du SHA-256
- **Déterministe** : Même entrée → même sortie
- **Non réversible** : Impossible de retrouver l'entrée depuis le hash
- **Résistant aux collisions** : Difficile de trouver deux entrées avec même hash
- **Effet avalanche** : Petit changement → grand changement dans le hash

### Avantages des Arbres de Merkle
- **Efficacité** : Vérification rapide avec logarithme de complexité
- **Intégrité** : Toute modification est détectable
- **Preuve concise** : Preuves d'inclusion compactes
- **Scalabilité** : Adapté aux grands ensembles de données

## 📖 Applications Réelles

Ces concepts fondamentaux sont utilisés dans :
- **Bitcoin et Ethereum** : Validation des transactions
- **Systèmes de fichiers** : Intégrité des données (IPFS)
- **Certificats numériques** : Chaînes de confiance
- **Voting électronique** : Intégrité des votes

## 🤝 Contribuer

Ce projet est à but éducatif. N'hésitez pas à :
- Signaler des erreurs ou améliorations
- Ajouter de nouveaux exercices
- Proposer des clarifications pédagogiques

## 📄 Licence

Projet éducatif libre pour l'apprentissage de la blockchain.

---

**Auteur** : Développé dans le cadre d'exercices pédagogiques sur la blockchain  
**Niveau** : Débutant/Intermédiaire  
**Durée estimée** : 2-3 heures pour comprendre tous les concepts