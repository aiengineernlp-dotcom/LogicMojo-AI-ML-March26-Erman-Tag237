import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from feature_engineering import r_create_other_features

# i will use only numeric column of my r_create_other_features
df_numeric = r_create_other_features.select_dtypes(include='number')
plt.figure(figsize=(12,8))
sns.heatmap(df_numeric.corr(), annot=False, cmap='coolwarm')
plt.title("hidding link in my 46 columns")
plt.show()