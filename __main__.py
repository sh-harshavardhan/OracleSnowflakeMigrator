# from oracle_trans.SchemaGenerator import SchemaGenerator as ora_ddl_generator
from snowflake_trans.DDLGenerator import DDLGenerator as snow_ddl_generator
# ora_ddl_generator().extract_schema()
snow_ddl_generator().generate_ddls()




