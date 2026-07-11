from config.settings import *
# ════════════════════════════════════════════════════
# STEP 1 — Push data to postgresSQL   # SITUATION: I have data from differents sources
# ════════════════════════════════════════════════════
# SITUATION: I have data from differents sources
# connection to postgresql
# Format : engine = create_engine('postgresql://utilisateur:motdepasse@localhost:5432/nom_de_ta_base')


engine = create_engine('postgresql://postgres:postgres@localhost:5551/datasphere360_customer_ecommerce')

if engine:
    print('Connected to PostgreSQL')
else:
    print('Not Connected to PostgreSQL')

def push_data_to_sql(csv_filepath: str, table_name: str) -> str:
    """
    :param csv_filepath:
    :param table_name:
    :return:

    """
    if not csv_filepath:
        # si le fichier n'existe pas , on pert pas le temps on block le programme avec raise
        raise ValueError("❌ Chemin de fichier incorrect ou pas trouvee! ")
    else:
        # si le fichier exsite
        try:
            df = pd.read_csv(csv_filepath)
            table_name = os.path.splitext(os.path.basename(csv_filepath))[0]  # la sortie ici sera juste le nom de la table sans extension ".csv"
            df.to_sql(table_name, con=engine, if_exists='replace', index=False)
            what_is_up = f"✅ Table {table_name} a ete creer !"
        except Exception as e:
            what_is_up = f"❌ Table {table_name} pas creer !❌ -> "f" L'erreur est {e}"

    return what_is_up




