import pandas as pd
import numpy as np
import seaborn as sns

data = sns.load_dataset("titanic")


def Featuretransformation(data: pd.DataFrame) -> pd.DataFrame:
    if data is not None:
        df = pd.DataFrame(data)

    age_group_c = df.groupby('who')['age']
    # age_group_a = df['Adult']
    # age_group__s =  df['Senior']

    return df


r = Featuretransformation(data)

print(r)

print(f"{"█" * 70} ANALYSIS {"█" * 60}")

print(f"{"█" * 70} Explain {"█" * 60}")
# print(f"Impact on overfitting and model performance")
# print(f"the impact of overfitting is that the model knows too much about data that he is suppose to learn from. ........")
