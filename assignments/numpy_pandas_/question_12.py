import pandas as pd
import numpy as np
import seaborn as sns

data = sns.load_dataset("iris")


def FeatureSelection(data: pd.DataFrame) -> pd.DataFrame:
    if data is not None:
        df = pd.DataFrame(data)

    num_col = df.select_dtypes(include=np.number)
    # 1. Compute correlation matrix
    corrre_m = num_col.corr()

    # 2 Identify highly correlated features
    highly_correlated_features = ["petal_width"]

    # Drop redundant features
    df_reduced = df.drop(
        columns=highly_correlated_features)  # on supprime les colonnnes forteement correrler entre elles

    return df_reduced


r = FeatureSelection(data)

print(r)

print(f"{"█" * 70} ANALYSIS {"█" * 60}")

print(f"{"█" * 70} Explain {"█" * 60}")
print(f"Impact on overfitting and model performance")
print(
    f"the impact of overfitting is that the model knows too much about data that he is suppose to learn from. ........")
