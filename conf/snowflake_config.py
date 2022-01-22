snowflake_connection_details = {
    "username": "researchpapers57",
    "password": "Cisco@123",
    "account": "tx41467.ap-south-1.aws"
}

snowflake_db = "TEST"

get_schemas_list_query = 'SHOW SCHEMAS IN {}'.format(snowflake_db)

create_schema_query = 'CREATE SCHEMA IF NOT EXISTS {}'.format(snowflake_db) + '.{}'

add_pk_query = "ALTER TABLE {}".format(snowflake_db) + ".{}.{} ADD CONSTRAINT {} PRIMARY KEY ({})"

add_fk_query = "ALTER TABLE {0}.{1}.{2} ADD CONSTRAINT {3} FOREIGN KEY ({4}) REFERENCES {0}.{1}.{5} ({6})"
