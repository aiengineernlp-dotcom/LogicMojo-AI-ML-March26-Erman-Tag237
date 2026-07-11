# ════════════════════════════════════════════════════
#  — CLEAN
# ════════════════════════════════════════════════════
from config.settings import *

def handle_missing_values(raw_data_from_:dict)->dict:
    all_is_missing={}
    treshold = 0.3
    missing_values_great_30={}

    for table_name, df in raw_data_from_.items():
        if df.empty:
            raise ValueError("Donnees introuvables")
        else:
            try:
                df_clone = df.copy()
                for col_name in df_clone.columns:
                    col_value = df[col_name]
                    # -1- Missing Values
                    is_missing = col_value.isnull().sum()
                    if is_missing > 0:
                        all_is_missing[table_name] = is_missing
                    # -2- more than 30% missing values
                    more_than_30 = is_missing > (treshold * len(df_clone))
                    if more_than_30:
                        missing_values_great_30[col_name] = is_missing
                    else:
                        if is_missing > 0:
                            # -3- base on type of variable, I will transform missing values to :
                            # - 3.1 - Median for numerical  variables,
                            if pd.api.types.is_numeric_dtype(col_value):
                                # compute the median
                                median_col_value = col_value.median()
                                # Replace by the median
                                df_clone[col_name] = col_value.fillna(median_col_value)
                                # print(f"Numerical:{col_name} - Median is : {median_col_value}")

                            #- 3.2 Mode for categorial variables
                            elif pd.api.types.is_object_dtype(col_value) or pd.api.types.is_categorical_dtype(col_value):
                                # compute the mode
                                mode_col_value = col_value.mode()[0] #  [0] because .mode() always return a list. and i can not put a list in a dataframe (exel file) so i just take the first value
                                # Replace by the mode (la valeur la plus frequente)
                                df_clone[col_name] = col_value.fillna(mode_col_value)
                                # print(f"categorial:{col_name} - mode is: {mode_col_value}\n")
                        else:
                            # print(f"🟢 {col_name} : all is fine")
                            print()
            except Exception as e:
                print("STOP l'erreur est : ->", e)

    return  raw_data_from_




def remove_duplicated_record(raw_data_from_: dict):
    duplicated_records = {}

    for table_name, df in raw_data_from_.items():
        if df.empty:
            raise ValueError("Donnnees non trouvees")
        else:
            try:
                df_clone = df.copy()
                for col_name in df_clone.columns:  # id , name , sexe , city
                    # 🚩col_value = df[col_name]
                    # 🚩if col_value.duplicated().any(): # BAS: col_value est une Series (une colonne) or on veux une ligne qui correspond a un record.  Donc col_value.duplicated() vérifie si des valeurs de cette colonne sont répétées. C'est pas ce que on veux. On veut savoir et voir les LIGNES (record) Dupliquees
                    pass
                duplicates = df_clone[df_clone.duplicated()]

                if not duplicates.empty:
                    duplicated_records[table_name] = duplicates
            except Exception as e:
                print("The error is ", e)

    return duplicated_records



def convert_date_col_to_date_time_format(raw_data_from_: dict):
    converted_columns = []
    converted_tables = {}

    for table_name, df in raw_data_from_.items():
        if df.empty:
            raise ValueError("Donnees nont trouvees")
        else:
            try:
                df_clone = df.copy()
                for col_name in df_clone.columns:
                    if pd.api.types.is_datetime64_any_dtype(df_clone[col_name]) or pd.api.types.is_datetime64_dtype(
                            df_clone[col_name]):
                        print(f" {col_name} already converted ")
                        continue
                    if 'date' in col_name.lower() or 'datetime' in col_name.lower():
                        df_clone[col_name] = pd.to_datetime(df_clone[col_name],
                                                            errors="coerce")  # errors="coerce" pour dire que si une valeur ne peut pas etre convertie ne plante pas
                        converted_columns.append(col_name)  # liste des colonnes converties
                converted_tables[
                    table_name] = df_clone  # Veut dire Dans le casier "customers", je mets le DataFrame df_clone; ici df_clone n’est PLUS une copie, c’est juste une valeur stockée dans un dictionnaire
                '''
                df_clone est un DataFrame
                converted_tables["customers"] = df_clone est juste le stockage de ce DataFrame dans un dictionnaire
                '''

            except Exception as e:
                print(f"🛑 L'erreur  est ici :  {e} 👈 ")

    return converted_tables, converted_columns



def validate_data_type_and_range(raw_data_from_: dict, expected_schema: dict) -> dict | bool:
    final_report = {}
    for table_name, df in raw_data_from_.items():
        if df.empty:
            raise ValueError("Pas de donnees")
        else:
            try:
                df_clone = df.copy()
                for col_name in df_clone.columns:
                    results = {
                        "column": col_name,
                        "errors": []
                    }


                    table_schema = expected_schema.get(table_name,
                                                       {})

                    col_rules = table_schema.get(col_name,
                                                 {})
                    expected_type = col_rules.get("type")
                    min_val = col_rules.get("min")
                    max_val = col_rules.get("max")

                    # 0. vérifier le type réel
                    if expected_type is None:
                        results["errors"].append("Colonne non définie dans schema")
                        final_report[f"{table_name}.{col_name}"] = results["errors"]
                        # raise ValueError(f"Colonne {col_name} non définie dans le schema") # Ça rend ton moteur :trop strict, pas flexible, pas “data pipeline friendly”
                        continue

                    # 1. NUMERIC
                    if expected_type == "numeric":
                        if not pd.api.types.is_numeric_dtype(df_clone[col_name]):
                            results["errors"].append(f"{col_name} n'est pas numérique")

                        # 1.1. min
                        if min_val is not None and df_clone[col_name].min() < min_val:
                            results["errors"].append("Valeur min dépassée")

                        # 1.2. max
                        if max_val is not None and df_clone[col_name].max() > max_val:
                            results["errors"].append("Valeur max dépassée")

                    # 2. TEXT
                    elif expected_type == "text":
                        if not pd.api.types.is_object_dtype(df_clone[col_name]):
                            results["errors"].append("Type non texte")

                    # 3. DATETIME
                    elif expected_type == "datetime":
                        if not pd.api.types.is_datetime64_any_dtype(df_clone[col_name]):
                            results["errors"].append("Type non datetime")

                    # 4. MISSING (TOUS TYPES)
                    missing_count = df_clone[col_name].isnull().sum()
                    if missing_count > 0:
                        results["errors"].append(f"{missing_count} valeurs manquantes")

                    # 5. STORE RESULT

                    if results["errors"]:
                        final_report[f"{table_name}.{col_name}"] = results['errors']
                        print(f"❌ Error on the results {results['errors']}, for the columns {results['column']}  ")
                    else:
                        print(f"{col_name} ✅  YOU are good to go data validated!!")
            except Exception as e:

                print(f"L'erreur est {e}")
    return final_report


# need tu put my real column in the schema not yet done ( later please)
expected_schema = {

    "customers": {

        "customer_id": {
            "type": "numeric",
            "required": True,
            "unique": True,
            "min": 1
        },

        "name": {
            "type": "text",
            "required": True
        },

        "birth_date": {
            "type": "datetime"
        },

        "salary": {
            "type": "numeric",
            "min": 0,
            "max": 100000
        }

    },

    "orders": {

        "id": {
            "type": "numeric",
            "unique": True
        },

        "amount": {
            "type": "numeric",
            "min": 0
        },

        "order_date": {
            "type": "datetime"
        }

    }

}



def standardize_col_name(raw_data_from_: dict) -> dict:
    cleaned_data = {}
    for table_name, df in raw_data_from_.items():
        if df.empty:
            raise ValueError("Pas de donnees")
        else:
            try:
                df_clone = df.copy()
                df_clone.columns = (df_clone.columns
                                    .str.strip()
                                    .str.lower()
                                    .str.replace(' ', '_', regex=False)
                                    .str.replace('.', '_', regex=False))
                cleaned_data[table_name] = df_clone
                print(f"Column standartized for the table:  {table_name}")
                # pense a  affiche le avant et le apres :)
            except Exception as e:
                print(f"L'erreur est {e}")

    return raw_data_from_




def cleaning(raw_data_from_:dict):
    print(f"\n🧹 CLEANING")

    colonnes_numeriques = []
    colonnes_texte = []
    cleaned_data={}
    for table_name, df in raw_data_from_.items():
        if df.empty:
            # print("ok")
            raise ValueError("Erman The data is not avaible")
        else:
            # print("ok_1")
            try:
                raw_data_from_clean = df.copy()
                for col in raw_data_from_clean.columns:
                    # print("ok_4")
                    # colonnes numériques
                    if raw_data_from_clean[col].dtype in ["int64", "float64"] or pd.api.types.is_numeric_dtype(
                            raw_data_from_clean[col]):  ## C"EST CA QUE JE VAIS FUSIONNER L"INGINE FINALE
                        raw_data_from_clean[col] = raw_data_from_clean[col].fillna(raw_data_from_clean[col].median())
                        colonnes_numeriques.append(col)
                        # print(colonnes_numeriques)

                    # colonnes texte
                    if raw_data_from_clean[col].dtype == "object" or pd.api.types.is_object_dtype(
                            raw_data_from_clean[col]) or pd.api.types.is_categorical_dtype(
                            raw_data_from_clean[col]):  ## C"EST CA QUE JE VAIS FUSIONNER L"INGINE FINALE
                        raw_data_from_clean[col] = raw_data_from_clean[col].fillna(raw_data_from_clean[col].mode()[0])
                        colonnes_texte.append(col)
                        # print(colonnes_texte)
                    # more than 30% missing values  a coder
                    # if raw_data_from_clean[col].isnull():
                cleaned_data[table_name] = raw_data_from_clean
            except Exception as e:
                print(f"Erman The error is {e}")

    return cleaned_data


if __name__ == "__main__":
    pass




