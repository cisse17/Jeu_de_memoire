
# ______Code initial 1ere VERSION______

"""import random
import time
import os
sequence = ""

def nettoyer_ecran():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


for i in range(4):
    sequence += str(random.randint(0, 9))

score = 0
while True:
    print("Bienvenu sur votre jeu de memoire")
    print("Retenez la sequence")
    time.sleep(2)
    nettoyer_ecran()
    print(sequence)
    time.sleep(2)
    nettoyer_ecran()

    reponse_utilisateur = input("Quelle est la sequence ?")
    if sequence == reponse_utilisateur:
        score += 1
        print("Bonne reponse votre score", score)
        sequence += str(random.randint(0, 9))
    else:
        score -= 1
        if score <= 0:
            break
        print("Mauvaise réponse, reessayer")
    time.sleep(2)
    nettoyer_ecran()

print("Votre score final", score)
   """ 

# ______ Optimisation code 2ere VERSION et Ajout de nouvelle chose ______

import random
import time
import os

NIVEAUX_JEU = (
    {
        "Titre": "Facile",
        "sequence_initiale_a_generer": 2,
        "incrementation_seq": 1,
        "duree_visualisation_chiffre": 2,
        "nbre_vies": 3,
     },
    {
        "Titre": "Moyen",
        "sequence_initiale_a_generer": 3,
        "incrementation_seq": 1,
        "duree_visualisation_chiffre": 2,
        "nbre_vies": 2,
     },
    {
        "Titre": "Difficile",
        "sequence_initiale_a_generer": 3,
        "incrementation_seq": 2,
        "duree_visualisation_chiffre": 1,
        "nbre_vies": 1,
     },
)

def nettoyer_ecran():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def generer_sequence(n):
    sequence = ""
    for i in range(n):
        sequence += str(random.randint(0, 9))
    return sequence


def demander_reponse_numerique_min_et_max(min, max):
    reponse_str = input("Choisissez votre niveau entre " + str(min) + " et " + str(max) + " : " )
    try:
        reponse_int = int(reponse_str)
    except:
        print("ERREUR : Vous devez rentrer une valeur numérique")
        return demander_reponse_numerique_min_et_max(min, max)

    if not min <= reponse_int <= max:
        print("ERREUR : Vous devez rentrer une valeur entre ", min, " et ", max)
        return demander_reponse_numerique_min_et_max(min, max)
     
    return reponse_int

def recuperer_data_niveau_jeu(niveaux):
    print(" ____________________________________")
    print("|                                    |")
    print("| Bienvenu sur votre jeu de memoire  |") 
    print("|____________________________________|")
    print()
    index = 1
    for niveau in niveaux:
        print(f"   {index} - {niveau['Titre']}") 
        index += 1
        print()

    choix = demander_reponse_numerique_min_et_max(1, len(niveaux))
    return niveaux[choix - 1]

data_niveaux_ieu = recuperer_data_niveau_jeu(NIVEAUX_JEU)

sequence = generer_sequence(data_niveaux_ieu["sequence_initiale_a_generer"])


nbre_vie = data_niveaux_ieu['nbre_vies']
score = 0


# Programme principal
while True:
    # print(f"Vous avez droit {nbre_vie} essaie(s)")
    print(f"Il vous reste {nbre_vie} vie(s)")
    time.sleep(2)
    print("Retenez la sequence")
    time.sleep(data_niveaux_ieu["duree_visualisation_chiffre"])
    nettoyer_ecran()
    print(sequence)
    time.sleep(data_niveaux_ieu["duree_visualisation_chiffre"])
    nettoyer_ecran()

    reponse_utilisateur = input("Quelle est la sequence ?")
    if sequence == reponse_utilisateur:
        score += 1
        print("Bonne reponse votre score", score)
        sequence += generer_sequence(data_niveaux_ieu["incrementation_seq"])
    else:
        nbre_vie -= 1
        if nbre_vie <= 0:
            break
        print("Mauvaise réponse, réessayer")
    time.sleep(2)
    nettoyer_ecran()

print()
print(f"Mauvaise réponse, la séquence était : {sequence}")
print("Votre score final", score)
print()
