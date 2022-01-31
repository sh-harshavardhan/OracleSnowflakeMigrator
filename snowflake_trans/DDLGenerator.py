import json
import logging
import glob
import os
from pathlib import Path
from conf import ora_snow_datatype_mapping as osdm
from conf import snowflake_config as snow_conf
from snowflake_trans.Connection import Connection


class DDLGenerator:
    conn_obj = Connection()
    snow_conn = conn_obj.get_connection()

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def generate_ddls(self):
        """
        :Description : to convert json files to .ddl files compatable with snowflake
        """
        ora_schema_files = glob.glob('metadata/oracle/raw/*.json')
        self.logger.info("Converting the JSON files to .ddl s")
        for json_file in ora_schema_files:
            self.from_json_to_ddl(json_file)

    def from_json_to_ddl(self, filename):
        """
        :Description : convert each json file to ddl file compatable with snowflake
        :param filename: file to be converted to ddl
        """
        self.logger.info("Converting :: {} ...".format(filename))
        with open(filename, 'r') as json_fp:
            try:
                ddl_meta = json.loads(json_fp.read())
            except Exception as e:
                self.logger.error("Failed to parse the JSON file ::{}".format(filename))
                print(e)
                exit(1)

        # 0. GENERATE THE DDL
        DDL_CMD = ""

        # 1. CREATE STATEMENT
        DDL_CMD += "CREATE OR REPLACE TABLE {}.{}.{} (".format(snow_conf.snowflake_db,
                                                               ddl_meta.get('db'),
                                                               ddl_meta.get("table"))

        # 2. COLUMN ADDITION
        for col in ddl_meta.get('columns'):
            DDL_CMD += self.get_snowflake_column_def(col)

        # 3. REMOVE LAST ',' AND END OF COLUMN ADDITION
        DDL_CMD = DDL_CMD[:-1]
        DDL_CMD += ')'

        # 4. CONSTRAINT ADDITION
        # for costraint in ddl_meta.get('constraints'):
        #     DDL_CMD += self.get_snowflake_constraint_def(costraint)

        output_ddl_location = 'metadata/snowflake/ddl/' + Path(filename).stem + '.ddl'
        os.makedirs(os.path.dirname(output_ddl_location), exist_ok=True)
        with open(output_ddl_location, 'w') as ddl_fp:
            ddl_fp.write(DDL_CMD)

    def get_snowflake_column_def(self, col_details):
        """
        :Description : convert oracle datatype to snowflake datatype
        :param col_details: oracle datatype
        :return: snowflake compatable datatype
        """

        isNullable = "NOT NULL" if col_details.get("NULLABLE") == "Y" else ""
        datatype = osdm.ora_snow_datatype_mapping.get(col_details.get("DATA_TYPE"))
        if col_details.get("DATA_TYPE") in ("VARCHAR2", "NVARCHAR2", "CHAR", "NCHAR"):
            precision_or_length = col_details.get("DATA_LENGTH")
        else:
            precision_or_length = col_details.get("DATA_PRECISION")

        if bool(col_details.get("DATA_PRECISION")):
            if bool(col_details.get("DATA_SCALE")):
                # with precision and scale
                return "\n{} {}({},{}) {},".format(col_details.get("COLUMN_NAME"),
                                                   datatype,
                                                   col_details.get("DATA_PRECISION"),
                                                   col_details.get("DATA_SCALE"),
                                                   isNullable)
            elif bool(col_details.get("DATA_PRECISION")):
                # with only precision/length
                return "\n{} {}({}) {},".format(col_details.get("COLUMN_NAME"),
                                                datatype,
                                                precision_or_length,
                                                isNullable)
        else:
            # without precision and scale
            return "\n{} {} {},".format(col_details.get("COLUMN_NAME"), datatype, isNullable)


