import pandas as pd
import numpy as np
import seaborn as erman

data = erman.load_dataset("titanic")


def manage_feature_engineering(data: pd.DataFrame):
    """

    """
    if data is not None:
        df = pd.DataFrame(data)
    # family_size feature
    family_size = df['sibsp'] + df['parch'] + 1
    # is_alone feature
    is_alone = df['alone']
    is_alone_survival = df[df['alone'] == True]  # On filtre pour n'avoir que les personnes seules
    # Compute survival_rate by is_alone --> donc on calcule le taux de survie a partir de is_alone
    survival_rate = is_alone_survival['survived'].mean()
    return family_size, is_alone_survival, survival_rate, is_alone


family_size, is_alone_survival, survival_rate, is_alone = manage_feature_engineering(data)

print(f"{"█" * 70} TEST RESULTS {"█" * 55}")

print(f" family_size:")
print(f'{'-' * 50}')
print(f"{family_size}\n")
# ====================
print(f" is_alone:")
print(f'{'-' * 50}')
print(f" is alone ? : {is_alone}\n")
# ====================
print(f'{'-' * 50}')
print(f" is alone survival base on True:  {is_alone_survival}\n")
# ====================
print(f'{'-' * 50}')
print(f" survival rate base on survival (is_alone = True):\n{survival_rate}\n")
# ====================
print(f'{'-' * 50}')

print(f"{"█" * 70} ANALYSIS {"█" * 60}")
print("Why engineered features improve ML models")
print(
    " ==>> engineered features improve ML models beacause it helps to reduice some features and combine them so the Ml model will be more efficient and fast ")
