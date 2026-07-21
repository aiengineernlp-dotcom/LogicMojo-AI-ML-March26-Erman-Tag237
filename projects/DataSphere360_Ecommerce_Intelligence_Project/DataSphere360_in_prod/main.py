from config.settings import engine
from data.loader import fech_data_from_psql
from analysis.explorer_eda_1 import data_overview, understanding_relation_between_tables
from data.cleaner import cleaning
from data.data_integration import data_integration
from data.feature_eng_auto import f_feature_engineering
from data.feature_eng_manu import f_feature_eng_manu
from data.eda_auto import f_generate_eda_report
from data.eda_manu import f_generate_eda_metier_report

# Step 1 - Fetch
raw_data = fech_data_from_psql(engine)


# Step 2 - EDA 1 (observation)
data_overview(raw_data)
understanding_relation_between_tables(raw_data)

# Step 3 - Cleaning
clean_data = cleaning(raw_data)

# Step 4 - Integration
integrated_data = data_integration(clean_data)

# Step 5 - Feature Engineering Auto
features_auto = f_feature_engineering(integrated_data)

# Step 6 - Feature Engineering Manuel
df_final = f_feature_eng_manu(features_auto)

# Step 7 - EDA Auto
f_generate_eda_report(df_final, "output/reports/eda_auto_report.html")

# Step 8 - EDA Métier
f_generate_eda_metier_report(df_final, "output/reports/eda_metier_report.html")