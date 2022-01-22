from oracle_trans.SchemaExtractor import SchemaExtractor as ora_ddl_gene
from snowflake_trans.SchemaCreator import SchemaCreator as sch_crt
from snowflake_trans.DDLGenerator import DDLGenerator as ddl_gen

if __name__ == '__main__':
    ora_ddl_gene().extract_schema()
    ddl_gen().generate_ddls()
    sch_crt().generate_snowflake_schema()


def test_setup():
    print("hello")
