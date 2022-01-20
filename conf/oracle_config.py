oracle_connection_details = {
    "server": "tcps://adb.ap-hyderabad-1.oraclecloud.com?wallet_location=c:\\Users\\ekhar\\Downloads\\Wallet_sandboxdb",
    "username": "ADMIN",
    "password": "Hindupur!123",
    "service": "g674a77d814dfc7_sandboxdb_high.adb.oraclecloud.com",
    "port": 1522,
    "dsn": "sandboxdb_high"
}

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

get_dbs_list_query = "select username from ALL_USERS where REGEXP_LIKE(username,'{}')"
get_tables_list_query = "SELECT owner || '.' || table_name  from all_tables where owner = '{}'"
get_column_list_query = "select column_name,data_type, data_precision, data_scale, nullable " \
                            "from ALL_TAB_COLUMNS " \
                            "where TABLE_NAME = '{}' and owner = '{}'"