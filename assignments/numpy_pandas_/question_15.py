import pandas as pd
import numpy as np
import seaborn as sns

data = sns.load_dataset('tips')


def Insight_Problem(data: pd.DataFrame) -> pd.DataFrame:
    """
    Use case:
        -
        -
    Args:
        -
        -
    Returns:
        -
        -
    Error:
        -
        -
    """
    if data is not None:
        df = pd.DataFrame(data)
    else:
        pass

    # tip_percentage
    df['tip_percentage'] = (df['tip'] / df['total_bill']) * 100
    # 2. Group tip_percentage by day and time:
    df['tip_percentage_by_day_and_time'] = df.groupby(['day', 'time'], observed=True)['tip_percentage'].transform(
        'mean')  # .transform is use to conserve data on lines. since im adding informations to DataFrame

    # Highest revenue segment
    revenue_by_day = df.groupby('day')['total_bill'].sum()
    highest_day = revenue_by_day.idxmax()
    max_revenue = revenue_by_day.max()

    return highest_day


r = Insight_Problem(data)

print(r)
print(f"{"█" * 70} ANALYSIS {"█" * 60}")

print(f"{"█" * 70} Explain {"█" * 60}")
print(f"Recommendation for business strategy")
print(f" -saturday and thursday are the benificial day where there is a lot of sales ")