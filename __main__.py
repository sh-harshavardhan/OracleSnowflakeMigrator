from oracle_trans.SchemaExtractor import SchemaExtractor as ora_ddl_gene
from snowflake_trans.SchemaCreator import SchemaCreator as sch_crt
from snowflake_trans.DDLGenerator import DDLGenerator as ddl_gen

if __name__ == '__main__':

    # to generate .json files from Oracle schema
    ora_ddl_gene().extract_schema()

    # to convert the .json files to .ddl files compatible with snowflake
    ddl_gen().generate_ddls()

    # to create snowflake schemas and run the .ddl files.
    sch_crt().generate_snowflake_schema()


