
from data.cleaner import r_c_cleaning
from data.data_iintegration_je_doute_de_location import data_integration
from data.feature import f_feature_engineering

r_data_integration = data_integration(r_c_cleaning)
r_features = f_feature_engineering(r_data_integration)

print(r_features.columns.tolist())
print(r_features.shape)