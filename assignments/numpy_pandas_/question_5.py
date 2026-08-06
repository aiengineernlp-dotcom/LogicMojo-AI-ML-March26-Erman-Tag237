import numpy as np
import pandas as pd
import seaborn as sns

data = sns.load_dataset("titanic")


# print(data)

def filter_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    This function is for Filtering Data for Business Logic

    Args:
        - data: full titanic dataset imported with seaborn
        -
    Returns:
        - DataFrame ready to take or make decision
        -
    Errors:
        - Exceoption Error
        - ValuesError
    """
    if data is not None:
        try:
            df = pd.DataFrame(data)
        except [Exception, ValueError] as e:
            raise ValueError(f" Must have a data to continue operarions {e} ")
    by_female_and_first_class = df[(df['sex'] == "female") & (df['class'] == "First")]
    # Survival rate for this group
    female_first_survived_rate = by_female_and_first_class['survived'].sum()
    # overall survival rate
    titanic_survival_rate = df['survived'].sum()
    # titanic survival rate exclude women in first class
    tit_sur_ex_wom_f_class = titanic_survival_rate - female_first_survived_rate
    return by_female_and_first_class, female_first_survived_rate, titanic_survival_rate, tit_sur_ex_wom_f_class


by_female_and_first_class, female_first_survived_rate, titanic_survival_rate, tit_sur_ex_wom_f_class = filter_data(data)

print(f"{"█" * 70} TEST RESULTS {"█" * 55}")
print(data)
print(f" Female passengers in 1st class:")
print(f'{'-' * 50}')
print(f"{by_female_and_first_class}\n")
# ====================
print(f" Computation: Survival rate for this group:")
print(f'{'-' * 50}')
print(f"{female_first_survived_rate}\n")
# ====================
print(f"overall survival rate:")
print(f'{'-' * 50}')
print(f"{titanic_survival_rate}\n")
print(f'{'-' * 50}')
print(f"titanic survival rate exclude women in first class:\n{tit_sur_ex_wom_f_class}\n")
# ====================
print(f"{"█" * 70} INTERPRETATION OF RESULTS {"█" * 42}")
print(f"What insight can be used in ML feature engineering?")
print("the insight who can be use in ML feature engineering is 'who' because he has (3) entities")


