oracle_connection_details = {
    "username": "ADMIN",
    "password": "Hindupur!123",
    "dsn": "sandboxdb_high"
}

oracle_client_dir = r"C:\oraClient\instantclient_19_9"

"""
List of Owners/Schemas/Databases to consider
    - if  oracle_db_inclusion_list is empty and oracle_db_exclusion_list is empty 
        : all schemas are considered
    - if  oracle_db_inclusion_list is empty and oracle_db_exclusion_list is not empty 
        : all schemas are considered except tables listed in oracle_db_inclusion_list
    - if  oracle_db_inclusion_list is not empty and oracle_db_exclusion_list is empty 
        : only schemas mentioned in oracle_db_inclusion_list are considered
    - if  oracle_db_inclusion_list is not empty and oracle_db_exclusion_list is not empty 
        : all schemas are considered except oracle_db_exclusion_list
"""

oracle_db_inclusion_list = []
oracle_db_exclusion_list = []

get_dbs_list_query = "SELECT USERNAME FROM ALL_USERS WHERE REGEXP_LIKE(USERNAME,'{}')"
get_tables_list_query = "SELECT TABLE_NAME  FROM ALL_TABLES WHERE OWNER = '{}'"
get_column_list_query = "SELECT COLUMN_NAME, DATA_TYPE, DATA_PRECISION, DATA_SCALE,DATA_LENGTH, NULLABLE " \
                        "FROM ALL_TAB_COLUMNS " \
                        "WHERE TABLE_NAME = '{}' AND OWNER = '{}'"
get_pk_constraint_list_query = "SELECT ACC.CONSTRAINT_NAME, ACC.COLUMN_NAME " \
                               "FROM ALL_CONSTRAINTS AC JOIN ALL_CONS_COLUMNS ACC " \
                               "ON ACC.OWNER = AC.OWNER " \
                               "AND ACC.CONSTRAINT_NAME = AC.CONSTRAINT_NAME " \
                               "WHERE AC.TABLE_NAME = '{}' AND AC.OWNER = '{}' " \
                               "AND AC.CONSTRAINT_TYPE = 'P'"
get_fk_constraint_list_query = "SELECT a.constraint_name, a.column_name parent_column, " \
                               "c_pk.table_name fk_table_name,  b.column_name fk_column_name   " \
                               "FROM ALL_CONS_COLUMNS a  " \
                               "JOIN ALL_CONSTRAINTS c " \
                               "ON a.owner = c.owner AND a.constraint_name = c.constraint_name   " \
                               "JOIN ALL_CONSTRAINTS c_pk " \
                               "ON c.r_owner = c_pk.owner AND c.r_constraint_name = c_pk.constraint_name   " \
                               "JOIN ALL_CONS_COLUMNS b " \
                               "ON C_PK.owner = b.owner AND C_PK.CONSTRAINT_NAME = b.constraint_name " \
                               "AND b.POSITION = a.POSITION      " \
                               "WHERE c.constraint_type = 'R'  and a.TABLE_NAME = '{}' AND a.OWNER = '{}' "
