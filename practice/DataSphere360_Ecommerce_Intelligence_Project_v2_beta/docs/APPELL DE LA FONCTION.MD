## APPELL DE LA FONCTION

supossons que j'ai une fonction_A() que j'ai ecrite et je veux l'utiliser dans une autre fonction_B(). je fais comment ?

je me dis que je dois appeller  A dans B. comme ceci:
- 1- dans la fonction A je fais le return "a" -> le resultat 
-2- j'apelle la fonction A. exemple: appel_de_A = fonction_A()  --> desormais si je veux exploiter le resultat 'a', je dois utiliser appel_de_A car c'est lui qui appelle la foction qui a son tour lance l'operation pour avoir le resultat 'a'. donc dans une autre fonction par exemple fonction_B() si je veux exploiter la fonction_A(), je vais juste utiliser appel_de_A.


C'est exactement la bonne logique ! Tu as très bien compris le concept de la valeur de retour.
Cependant, il y a une petite nuance technique sur où tu places ton appel. Voici les deux façons de faire :
## 1. La méthode directe (La plus courante)
Tu n'as pas besoin de créer une variable en dehors des fonctions. Tu appelles fonction_A() directement à l'intérieur de fonction_B().

def fonction_A():
    return "Résultat de A"
def fonction_B():
    # On récupère le résultat de A directement ici
    resultat_recu = fonction_A() 
    
    # On l'utilise pour faire autre chose
    phrase_finale = resultat_recu + " utilisé dans B"
    return phrase_finale

print(fonction_B()) # Affiche: Résultat de A utilisé dans B

## 2. Passer le résultat en argument (La plus flexible)
Si tu veux que fonction_B soit capable de travailler avec n'importe quel résultat (pas seulement celui de A), tu lui passes le résultat comme un "ingrédient".

def fonction_A():
    return "a"
def fonction_B(donnee):
    return f"J'exploite la donnée : {donnee}"
# 1. On stocke l'appelappel_de_A = fonction_A()
# 2. On donne ce résultat à B
print(fonction_B(appel_de_A))

## Pourquoi ta logique est bonne :
Quand tu dis : "je vais juste utiliser appel_de_A", c'est correct car appel_de_A devient le conteneur du résultat. C'est comme si fonction_A() était une usine :

   1. L'usine fabrique un objet (return).
   2. Tu mets l'objet dans un carton (appel_de_A = fonction_A()).
   3. Tu donnes le carton à une autre usine (fonction_B).

Attention au piège :
Si tu fais juste appel_de_A = fonction_A (sans les parenthèses ()), tu ne stockes pas le résultat "a", mais la fonction elle-même. N'oublie jamais les () pour déclencher l'opération !
Est-ce que tu veux voir comment faire si fonction_A a besoin de paramètres (des ingrédients) pour fonctionner ?



## PRTATIQUE

# def indentify_p_f_key(data_from_sql:dict)->str:
#     all_data = {}
#     unique = {}
#     potential_cols_save={}
#     pattern = re.compile(r'.*(id|pk|code|fk|pk).*',re.IGNORECASE)
#     for data_table in data_from_sql:
#         df = data_from_sql[data_table]
#         all_data[data_table] = df 

#     # I loop trougth my dictionnary all_data.item() to see if pattern regex is matching annd i save the result in  potential_cols
#     for data_table , df in all_data.items():
#         potential_cols = [col for col in df.columns if pattern.match(col)]
#         potential_cols_save[data_table] = potential_cols

#          # I will now use the unicity to verify if df[col].nunique() / len(df) == 1
#         for col in potential_cols:
#             is_unique = df[col].nunique() == len(df) # return True.  if for exemple i have in col : [p001,p002,p003], .nunique() will give me 3 and len(df) will also give me 3. 3==3 so its True and, col become my Primary Key (PK)
#             tipo = "PK (primary key)" if is_unique else "FK (Foreing Key)"
#             key = f"{data_table}.{col}"  #this line help to avoid loosing somme key because of collision. , also helo for the notation. if: data_table = "orders"  and col = "customer_id"  i will have -> key = "orders.customer_id"
#             unique[key] = tipo
#             print (f" Table {data_table} : Type Key Detected:  {tipo}  Key Name: {col} \n {'-' *50} ")
    
#     return unique
# indentify_p_f_key = indentify_p_f_key(fetch_dataSet) # note que ces donnees de mon dict sont deja de type "pandas" car j'ai utiliser "pandas.read_sql" pour la recuperation lors du fetch.

# print(f" ICI  {indentify_p_f_key}")

#--------------------
def data_integration(data_clean_from_sql: dict)-> dict:
    keys = f_indentify_p_f_key(data_clean_from_sql)
    
    for table_name, df in data_clean_from_sql.items():
        
        for col_name in df.columns:
            key_lookup = f"{table_name}.{col_name}"
            if key_lookup in keys:
                print(f"La colonne {col_name} est un {keys[key_lookup]}")
                
    return keys 
r_data_intagration = data_integration(data_clean_final)
print(r_data_intagration)













