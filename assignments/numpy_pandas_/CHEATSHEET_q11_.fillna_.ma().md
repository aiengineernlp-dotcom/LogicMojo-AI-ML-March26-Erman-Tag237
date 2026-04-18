## lorsque on me dit conver to numpy array on parle de quoi encore
Quand on te demande de "convert to numpy array", on parle de transformer ton objet (qui est souvent un DataFrame Pandas ou une liste) en un format matriciel pur : le ndarray.
## Pourquoi fait-on cela ?

   1. Performance : Les calculs mathématiques sont beaucoup plus rapides sur des tableaux NumPy que sur des objets Pandas.
   2. Compatibilité ML : La plupart des bibliothèques de Machine Learning (comme Scikit-Learn, PyTorch ou TensorFlow) n'acceptent pas les DataFrames directement ; elles exigent des tableaux NumPy en entrée.
   3. Perte des labels : Un tableau NumPy ne contient plus les noms des colonnes (age, fare) ni les index. Ce ne sont plus que des chiffres bruts dans une grille.

## Comment faire dans ton code ?
Il y a deux façons très simples de le faire à la fin de ta fonction :
Option A : La méthode moderne (recommandée)

# À la fin de ta fonctionreturn normalize.to_numpy()

Option B : L'attribut .values (très courant)

return normalize.values

## Ce que ça change visuellement :

* Avant (Pandas) : Tu vois un beau tableau avec des noms de colonnes et des numéros de lignes.
* Après (NumPy) : Tu vois uniquement des listes de listes de chiffres : [[ 0.22, -0.5], [ 1.4, 0.8]].

Attention : Une fois converti en NumPy, tu perds la capacité d'appeler les colonnes par leur nom (ex: df['age'] ne marchera plus). C'est pour ça qu'on le fait généralement à la toute dernière étape du pipeline.
Veux-tu que j'ajoute cette conversion finale à ta fonction pipeline_preprocessing ?

