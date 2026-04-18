
# QUESTION 8
## Étape 1 : Création de la colonne (Calcul du pourcentage inconnu)
df['tip_percentage'] = (df['tip'] / df['total_bill']) * 100

##Étape 2 : Remplissage des NaN (Imputation)
## On utilise la moyenne par jour que tu as calculée au début
df['tip_percentage'] = df['tip_percentage'].fillna(df['day'].map(average_tip_by_day))


C'est tout à fait normal d'être un peu perdu, car cette ligne combine trois concepts différents de Pandas. Décomposons-la étape par étape :
## 1. df['tip_percentage'] = ...

* Action : Tu crées ou tu mets à jour la colonne.
* Analogie : Tu désignes un casier vide (ou existant) où tu vas ranger le résultat final.

## 2. df['tip_percentage'].fillna(...)

* Action : "Cherche les trous (NaN) dans cette colonne et prépare-toi à les boucher."
* Le secret : .fillna() ne touche pas aux cases qui ont déjà un chiffre. Il ne s'occupe que du vide.

## 3. .map(average_tip_by_day)
C'est ici que la magie opère. Imagine que average_tip_by_day est un petit carnet d'adresses (un dictionnaire) :

* Sun : 3.20
* Sat : 3.10

L'action de .map() :
Pour chaque ligne de ton tableau, Pandas regarde la colonne day :

   1. Il voit "Sun".
   2. Il va voir dans ton carnet (average_tip_by_day) quelle est la valeur pour "Sun".
   3. Il récupère "3.20".
   4. .map() sert donc de traducteur ou de recherche automatique.

------------------------------
## Résumé de la phrase complète :

"Prends la colonne des pourcentages, et si tu trouves un vide, va regarder quel jour on est (.map) pour savoir quel chiffre de remplacement utiliser, puis enregistre tout ça."

------------------------------
## 💡 Un exemple visuel
Si ta ligne 12 a un pourcentage vide et que c'est un Samedi (Sat) :

* .fillna dit : "Vite, il me faut une valeur !"
* df['day'].map(...) regarde la colonne day, voit Sat.
* Il cherche Sat dans ta moyenne et trouve 3.10.
* Le vide est remplacé par 3.10.

------------------------------
## Pourquoi c'est mieux qu'une moyenne fixe ?
Si tu avais fait .fillna(3), tu aurais mis 3 partout. Avec .map(), tu mets la bonne moyenne pour le bon jour.
------------------------------
Pour t'aider à valider :

* Est-ce que l'idée du "carnet d'adresses" pour le .map() est plus claire ?
* Veux-tu qu'on regarde comment créer une catégorie (ex: "Petit", "Moyen", "Gros" pourboire) maintenant que tes calculs sont bons ?

To advance, would you like to:

* Classify these percentages?
* Summarize the final results by gender?


------------------------------

## calcule de pourcentages:

- pour trouver le montant on fait (axb)/100 --> car ici on trouve le montant a partir d'un pourcentage connu
- pour trouver le pourcentage on fait (a/b)x100 --> car ici on la les valeurs mais on doit trouver le pourcentage. Note a doit etre  a< b
        Ta règle d'or
            - Montant inconnu : On multiplie par le taux.
            - Pourcentage inconnu : On divise la partie par le tout.
                                    - Si a < b ton pourcentage sera entre 0% et 100%.
                                    - Si a > b le résultat sera supérieur à 100%. et on dira que le client est est ultra-généreux car a donné un pourboire plus grand que la facture 






