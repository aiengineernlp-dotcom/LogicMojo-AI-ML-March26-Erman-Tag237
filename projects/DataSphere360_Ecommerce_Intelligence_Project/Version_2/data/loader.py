from Version_2.config.settings import *

# importation des donnees from psql.
def fech_data_from_psql(connextion_to_psql: str) -> dict:
    """

    """
    if not connextion_to_psql:
        # if the connexion to psql doest not work
        raise ValueError("Failed to connnect at Psql")
    else:
        # if the connection to psql work then ...
        try:
            '''
            exactement ici je suis en train de creer un dictionnaire et pour ce faire j'ai besoin d'une clee valeur, alors 
            '''
            query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"  # me sert pour recuperer mes cles qui seront les noms puis en bas avec la boucle, for je charge le dictionnaire avec les valeurs
            tables = pd.read_sql(query, connextion_to_psql)['table_name'].to_list()
            all_data_fech_from_psql = {}
            for table in tables:
                query_table = f"SELECT * FROM {table}"  # for each table, i collect the content
                all_data_fech_from_psql[table] = pd.read_sql(query_table,
                                                             con=connextion_to_psql)  # then I field my dictionnary with the combo (key: values) created
            # print(tables)
        except Exception as e:
            print(f"the error is {e}")
    return all_data_fech_from_psql

if __name__ == "__main__":
    pass



