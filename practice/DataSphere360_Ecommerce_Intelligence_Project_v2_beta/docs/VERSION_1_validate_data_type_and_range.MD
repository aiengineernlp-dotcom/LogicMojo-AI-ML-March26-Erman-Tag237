


# ## VERSION -2-  validate_data_type_and_range    ONGOING WILL COME HERE LATER (I need to continue with a=other features) --> ref : docs/ VERSION_validate_data_type_and_range.MD

# def validate_data_type_and_range(data_clean:dict, rules:dict)->dict:
#     """
#     Use case : 
#         - Type validation (Verification) : Base on logic of how the type should be, we need to know if the the type expected is actually what we have. Exemple: df['age'] should ne type int64, not something else, 
#         - Range validation (Verification) : Base on logic of how the range should be, we need to know if we are in the normal range. Exemple df['age'] should not be up to 130. 
#         - 

#     Args:
#         - data_clean : 
#         - max_value: is the value that fit my need, the value that df[col_name] SHOULD NOT CROSS UP
#         - min_val : is the value that fit my need, the value that df[col_name] SHOULD NOT CROSS DOWN

#     Returns:
#         - dict:  report result 
#     """
#     final_results = {}
#     for col_name_in_rules_validations, specs in rules_validations.items(): # the col_name are in rules_validations that i created with the col_name present in my  df.columns
#        for col_name, df in data_clean.items():
#             if col_name in df.columns:
#                     expected_type = specs["type"]
#                     min_val = specs["min"]
#                     max_val = specs.get("max")

#                     if rules_validations in df.columns:
#                         errors = []

#                     if col_name_in_rules_validations not in final_results:
#                         results[col_name_in_rules_validations] ={}
                        
#                  # validation of type (Verification if the type that my col_name is same as expected)
#                     if not pd.api.types.is_dtype_equal(df[col_name].dtype, expected_type): # if type are not egual
#                         results['errors'].append(f"Type Error bro: Expected type is {expected_type} But receive is {df[col_name].dtype}")
        
#                     # validation of type (Verification if the range that my col_name has is  "normal or logic ")
#                     if pd.api.types.is_numeric_dtype(df[col_name]):
#                         if min_val is not None and (df[col_name].min() < min_val ):
#                             results['errors'].append(f"Min value of {col_name} out of range {df[col_name].min()}  < {min_val}")
        
#                         if max_value is not None and (df[col_name].max() > max_value):
#                             results['errors'].append(f"Max value of {col_name} out of range {df[col_name].max()}  > {max_value}")
        
#                     if not results["errors"]:
#                         print(f" {col_name}✅  YOU are good to go data validated!!  ")
#                     else:
#                         print(f"❌ Error on the results {results['errors']}, for the columns {results['Columns']} ")
            
#     return final_results
# rules_validations = {
#     "location" : {"type": "object", "min":10, "max":100},
#     "order_item" : {"type": "object", "min":10, "max":100},
#     "products":  {"type": "object", "min":10, "max":100},
#     "reviews": {"type": "object", "min":10, "max":100},
#     "sellers": {"type": "object", "min":10, "max":100},
#     "customers": {"type": "int64", "min":10, "max":100},
#     "category_translation": {"float64": "object", "min":10, "max":100},
#     "payments": {"type": "float64", "min":10, "max":100},
#     "orders": {"type": "int64", "min":10, "max":100},    
# }

# r = validate_data_type_and_range(convertion_to_datetime,rules_validations)  
# print(r)




-------------------- quest ce qui bloque ici .... Ce code ci haut 




    final_results = {}
    for col_name_in_rules_validations, specs in rules_validations.items(): # the col_name are in rules_validations that i created with the col_name present in my  df.columns
       for col_name, df in data_clean.items():
            if col_name in df.columns:
                    expected_type = specs["type"]
                    min_val = specs["min"]
                    max_val = specs.get("max")

                    if rules_validations in df.columns:
                        errors = []

                    if col_name_in_rules_validations not in final_results:
                        results[col_name_in_rules_validations] ={}
                        
                 # validation of type (Verification if the type that my col_name is same as expected)
                    if not pd.api.types.is_dtype_equal(df[col_name].dtype, expected_type): # if type are not egual
                        results['errors'].append(f"Type Error bro: Expected type is {expected_type} But receive is {df[col_name].dtype}")
        
                    # validation of type (Verification if the range that my col_name has is  "normal or logic ")
                    if pd.api.types.is_numeric_dtype(df[col_name]):
                        if min_val is not None and (df[col_name].min() < min_val ):
                            results['errors'].append(f"Min value of {col_name} out of range {df[col_name].min()}  < {min_val}")
        
                        if max_value is not None and (df[col_name].max() > max_value):
                            results['errors'].append(f"Max value of {col_name} out of range {df[col_name].max()}  > {max_value}")
        
                    if not results["errors"]:
                        print(f" {col_name}✅  YOU are good to go data validated!!  ")
                    else:
                        print(f"❌ Error on the results {results['errors']}, for the columns {results['Columns']} ")
            
    return final_results



## ===== Il y a 4 erreurs logiques et techniques majeures qui 


Il y a 4 erreurs logiques et techniques majeures qui bloquent ton code actuel. Voici précisément ce qui ne va pas et comment le corriger :
## 1. Le conflit de noms (col_name)
C'est le blocage principal. Dans ta deuxième boucle, tu écris for col_name, df in data_clean.items().

* Ici, col_name devient le nom de ta table (ex: "customers").
* Juste après, tu fais if col_name in df.columns. Python cherche donc si le nom "customers" est une colonne dans la table "customers". C'est presque toujours Faux.
* Correction : Utilise table_name pour la boucle des DataFrames.

## 2. L'erreur de dictionnaire (results vs final_results)
Tu initialises final_results = {} au début, mais à l'intérieur tu utilises un objet nommé results qui n'a jamais été créé.

* De plus, tu essaies de faire results['errors'].append(). Si la clé 'errors' n'existe pas encore, ton code va s'arrêter avec une KeyError.

## 3. La condition if rules_validations in df.columns
Cette ligne n'a pas de sens pour Python : rules_validations est un dictionnaire entier. Tu ne peux pas vérifier si un dictionnaire est "dans" les colonnes d'un DataFrame.

* Ce que tu voulais dire : if col_name_in_rules_validations in df.columns.

## 4. Variables non définies
Tu utilises max_value dans ton test, mais tu as défini la variable sous le nom max_val quelques lignes plus haut. Python va dire que max_value n'existe pas.
------------------------------
## Voici ton code corrigé pour qu'il fonctionne enfin :

def validate_data(data_clean, rules_validations):
    final_results = {}

    for col_rule, specs in rules_validations.items():
        for table_name, df in data_clean.items(): # table_name au lieu de col_name
            
            # On vérifie si la colonne de la règle existe dans ce DataFrame précis
            if col_rule in df.columns:
                # IMPORTANT : On crée une liste d'erreurs vide pour CETTE colonne
                errors = []
                
                expected_type = specs["type"]
                min_val = specs.get("min")
                max_val = specs.get("max")

                # 1. Validation de TYPE
                if not pd.api.types.is_dtype_equal(df[col_rule].dtype, expected_type):
                    errors.append(f"Type Error: Expected {expected_type}, got {df[col_rule].dtype}")
    
                # 2. Validation de RANGE
                if pd.api.types.is_numeric_dtype(df[col_rule]):
                    if min_val is not None and df[col_rule].min() < min_val:
                        errors.append(f"Min out of range: {df[col_rule].min()} < {min_val}")
    
                    if max_val is not None and df[col_rule].max() > max_val:
                        errors.append(f"Max out of range: {df[col_rule].max()} > {max_val}")
    
                # 3. Traitement des résultats
                if not errors:
                    print(f"✅ {table_name} > {col_rule}: Validated!")
                else:
                    print(f"❌ {table_name} > {col_rule}: {len(errors)} error(s) found.")
                    # On stocke dans final_results
                    if table_name not in final_results:
                        final_results[table_name] = {}
                    final_results[table_name][col_rule] = errors
            
    return final_results

## Pourquoi cette version marche ?

   1. Variables distinctes : col_rule (le nom de la colonne cherchée) et table_name (le nom du DataFrame actuel) ne se mélangent plus.
   2. Initialisation dynamique : On crée errors = [] à chaque tour. Si la liste reste vide, c'est que tout va bien.
   3. Dictionnaire imbriqué : final_results est maintenant organisé par table, puis par colonne. C'est beaucoup plus facile à exploiter.

Est-ce que tu vois pourquoi le fait d'avoir appelé ta table col_name empêchait Python de trouver tes vraies colonnes ?

