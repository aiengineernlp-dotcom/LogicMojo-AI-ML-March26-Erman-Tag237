import pandas as pd
import numpy as np
import seaborn as erman

data = erman.load_dataset('titanic')


def handle_null_values(data: pd.DataFrame) -> pd.DataFrame:
    """
    Use Case:This fonction is made to handle null values
    Context: Models can't works with null values

    Args:
        - data: full titanic dataset with null values load from seaborn
    Returns:
        - Clean dataset ready to be use by the model
    Errors:
        - Execption error
        - Value Error
        -
    """
    if data is not None:
        try:
            # Convert data to pd.DataFrame so i can easily use pandas operartions
            df = pd.DataFrame(data)
        except Exception as e:
            raise ValueNotFoundError(f" Need data to continue the ioperation {e} ")
    # Fill missing age using median of age.
    # 1- calculate the median of age first
    df_age_median = df['age'].median()
    # 2- replace the null value by the df_age_median
    df_median_filled = df["age"].fillna(df_age_median)
    # Fill missing embarked using mode
    # 1- claculate de mode of embarked first
    df_embarked_mode = df['embarked'].mode()[
        0]  # when i use [0] it's because i want to make sure to get the first value from de list. Thing about : myiste =[1,2,3,4][3] also ->[:top_k]
    # 2- filling embarked using mode
    df_embarked_filled = df['embarked'].fillna(df_embarked_mode)
    # Droping deck column because regarding .info() , it has 891-203 = 688 null value more than 30%.
    df_droping_deck = df['deck'].info()
    df_deck_droped = df['deck'].dropna()
    df_clean = df.fillna({
        "age": df_median_filled,
        "embarked": df_embarked_filled}
    )
    df_clean = df_clean.drop(columns=['deck'])

    return df_median_filled, df_embarked_filled, df_deck_droped, df_clean


df_median_filled, df_embarked_mode, df_deck_droped, df_clean = handle_null_values(data)

print(f"{"█" * 70} TEST RESULTS {"█" * 55}")
print(data)
print(f" 1-Fill missing age using median:")
print(f'{'-' * 50}')
print(f"{df_median_filled}\n")
# ====================
print(f" 2-Fill missing embarked using mode:")
print(f'{'-' * 50}')
print(f" embarked base on mode :  {df_embarked_mode}\n")
# ====================
print(f'{'-' * 50}')
print(f" Drop deck column")
print(f"{df_deck_droped}\n")
# ====================

print(f" Final clean data ready for ML:")
print(f'{'-' * 50}')
print(f"{df_clean}\n")
# ====================

print(f"{"█" * 70}  EXPLAINATION ANALYSIS {"█" * 60}")
print("Why different strategies are used for different columns")
print(
    " ==>>Because all columns provides differents data type for all those columns for exemple, age is int, embarked is string, and we are droping deck because it has 688/891 null values ")

""" ===> my Notes
fillna({...}) : C'est la méthode parfaite pour nettoyer plusieurs colonnes d'un coup.
.drop(columns=['nom']) : C'est le moyen standard pour retirer une colonne encombrante.
dropna() : On l'utilise généralement sur tout le DataFrame (df.dropna()) pour supprimer les lignes où il manque encore des infos après le nettoyage.
"""
