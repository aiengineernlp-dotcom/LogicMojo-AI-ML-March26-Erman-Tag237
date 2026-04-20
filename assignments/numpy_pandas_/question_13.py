import pandas as pd
import numpy as np
import seaborn as sns

data = sns.load_dataset("titanic")
print(data)
print("\n=======")


def Featuretransformation(data: pd.DataFrame) -> pd.DataFrame:
    if data is not None:
        df = pd.DataFrame(data)

    # 1. Create age_group:
    # Child / Adult / Senior
    age_group_c = df[df['age'] <= 10]
    age_group_a = df[(df['age'] > 10) & (df['age'] <= 50)]
    age_group__s = df[df['age'] > 50]

    # 2. Use .apply()

    # 3. Compute survival rate per group

    results = {}

    if len(age_group_c) > 0:
        results['rate_child'] = (age_group_c['survived'].sum() / len(age_group_c)) * 100

    if len(age_group_a) > 0:
        results['rate_adult'] = (age_group_a['survived'].sum() / len(age_group_a)) * 100

    if len(age_group__s) > 0:
        results['rate_senior'] = (age_group__s['survived'].sum() / len(age_group__s)) * 100

    return results


r = Featuretransformation(data)

print(r)

print(f"{"█" * 70} ANALYSIS {"█" * 60}")
print(f"Which segment has highest survival likelihood")
print(f"'rate_child': np.float64(59.375)")
print(f"{"█" * 70} Explain {"█" * 60}")

# --------------------------------------------------

