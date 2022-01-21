# from oracle_trans.SchemaGenerator import SchemaGenerator as ora_ddl_gene
from snowflake_trans.SchemaCreator import SchemaCreator
# ora_ddl_gene().extract_schema()


sch_creator = SchemaCreator()
sch_creator.generate_ddls()
# sch_creator.prep_snowflake()
# sch_creator.execute_ddls()




