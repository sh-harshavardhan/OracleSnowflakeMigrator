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
get_column_list_query = "SELECT COLUMN_NAME, DATA_TYPE, DATA_PRECISION, DATA_SCALE, NULLABLE " \
                        "FROM ALL_TAB_COLUMNS " \
                        "WHERE TABLE_NAME = '{}' AND OWNER = '{}'"
get_pk_constraint_list_query = "SELECT ACC.CONSTRAINT_NAME, ACC.COLUMN_NAME " \
                               "FROM ALL_CONSTRAINTS AC JOIN ALL_CONS_COLUMNS ACC " \
                               "ON ACC.OWNER = AC.OWNER " \
                               "AND ACC.CONSTRAINT_NAME = AC.CONSTRAINT_NAME " \
                               "WHERE AC.TABLE_NAME = '{}' AND AC.OWNER = '{}' " \
                               "AND AC.CONSTRAINT_TYPE = 'P'"
get_fk_constraint_list_query = "SELECT ACC.CONSTRAINT_NAME,ACC.COLUMN_NAME, AC_FK.TABLE_NAME,AC_FK.CONSTRAINT_NAME   " \
                               "FROM ALL_CONS_COLUMNS ACC JOIN ALL_CONSTRAINTS AC " \
                               "ON AC.OWNER= ACC.OWNER " \
                               "AND AC.CONSTRAINT_NAME = ACC.CONSTRAINT_NAME " \
                               "JOIN ALL_CONSTRAINTS AC_FK " \
                               "ON AC_FK.OWNER = AC.OWNER " \
                               "AND AC_FK.CONSTRAINT_NAME = AC.CONSTRAINT_NAME " \
                               "WHERE AC.TABLE_NAME = '{}' AND AC.OWNER = '{}' AND AC.CONSTRAINT_TYPE = 'R'"
