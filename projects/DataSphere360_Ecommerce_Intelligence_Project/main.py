
from data.cleaner import r_c_cleaning
from data.data_integration import data_integration
from data.feature_eng_auto import f_feature_engineering

r_data_integration = data_integration(r_c_cleaning)
r_features = f_feature_engineering(r_data_integration)

print(r_features.columns.tolist())
print(r_features.shape)