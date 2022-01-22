import json
import logging
import glob
from pathlib import Path
from conf import ora_snow_datatype_mapping as osdm
from conf import snowflake_config as snow_conf
from snowflake_trans.Connection import Connection


class SchemaCreator:
    conn_obj = Connection()
    snow_conn = conn_obj.get_connection()

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def generate_snowflake_schema(self):
        self.create_snowflake_schemas()
        self.execute_ddls()
        self.add_constraints()

    def create_snowflake_schemas(self):
        ora_schema_files = glob.glob('metadata/oracle/raw/*.json')
        self.logger.info("Converting the JSON files to .ddl s")
        schema_list = set()
        for json_file in ora_schema_files:
            with open(json_file, 'r') as json_file_fp:
                schema_list.add(json.loads(json_file_fp.read())["db"])
        yet_to_create_schemas = schema_list - self.get_snowflake_schemas()
        self.logger.info("Missing Schemas in snowflake, creating schemas :: \n{}"
                         .format("\n".join(yet_to_create_schemas)))
        for sch in yet_to_create_schemas:
            self.conn_obj.execute_snowflake_query(self.snow_conn,
                                                  snow_conf.create_schema_query.format(sch))

    def get_snowflake_schemas(self):
        results = self.conn_obj.query_snowflake_query(self.snow_conn, snow_conf.get_schemas_list_query, 1)
        schema_list = set()
        for row in results:
            schema_list.add(row[1])
        return schema_list

    def execute_ddls(self):
        """

        :return:
        """
        ddl_files = glob.glob('metadata/snowflake/ddl/*.ddl')
        for ddl_file in ddl_files:
            self.logger.info("Executing DDL :: {}".format(ddl_file))
            with open(ddl_file, 'r')as ddl_fp:
                self.conn_obj.execute_snowflake_query(self.snow_conn, ddl_fp.read())

    def add_constraints(self):
        ora_schema_files = glob.glob('metadata/oracle/raw/*.json')
        self.logger.info("Converting the JSON files to .ddl s")
        for json_file in ora_schema_files:
            with open(json_file, 'r') as json_file_fp:
                json_schema = json.loads(json_file_fp.read())

                if bool(json_schema.get("constraints")):
                    # 0. GENERATE THE DDL
                    for constraint in json_schema.get("constraints"):
                        for in_cons_key, in_cons_value in constraint.items():
                            if in_cons_value.get("CONSTRAINT_TYPE") == 'PK':
                                self.conn_obj.execute_snowflake_query(self.snow_conn, snow_conf.add_pk_query.format(
                                    json_schema.get("db"),
                                    json_schema.get("table"),
                                    in_cons_key,
                                    ",".join(in_cons_value.get("COLUMN_NAME"))))

                            elif in_cons_value.get("CONSTRAINT_TYPE") == 'FK':
                                self.conn_obj.execute_snowflake_query(self.snow_conn, snow_conf.add_fk_query.format(
                                    snow_conf.snowflake_db,
                                    json_schema.get("db"),
                                    json_schema.get("table"),
                                    in_cons_key,
                                    ",".join(in_cons_value.get("COLUMN_NAME")),
                                    in_cons_value.get("FK_TABLE_NAME"),
                                    ",".join(in_cons_value.get("FK_CONSTRAINT_NAME"))),
                                                                      0)

                else:
                    pass
