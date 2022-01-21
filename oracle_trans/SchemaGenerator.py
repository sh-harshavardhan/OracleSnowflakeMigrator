import json
import logging
import conf.oracle_config as ora_config
from oracle_trans.Connection import Connection







class SchemaGenerator:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def run_oracle_query(self,conn, query):
        """

        :param query:
        :param conn:
        :return:
        """
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            self.logger.error("Failed to Execute the query on Oracle")
            print(e)
            exit(1)

    def extract_schema(self):
        """

        :return:
        """
        conn_obj = Connection()
        conn = conn_obj.get_connection()

        db_list = self.get_databases_list(conn)
        self.logger.info("Below are the list of schemas found ::\n{}".format('\n'.join(db_list)))
        for db in db_list:
            table_list = self.get_table_list(conn, db)
            self.logger.info("Below are the list of table found in schema :: {}\n{}".format(db,
                                                                                            '\n'.join(table_list)))

            for table in table_list:
                self.logger.info("Fetching DDLs for {}.{}".format(db, table))
                master_details = dict()
                master_details['db'] = db
                master_details['table'] = table
                master_details['columns'] = self.get_column_details(conn, db, table)
                master_details['constraints'] = self.get_constraint_details(conn, db, table)

                with open('metadata/oracle/raw/{}.{}.json'.format(db, table), 'w') as ddl_fp:
                    ddl_fp.write(json.dumps(master_details, indent=3))


    def get_databases_list(self, conn):
        """
        :Description : To get the list of databases/schemas/owners based on the inclusive and exclusive list
        :param conn: Oracle connection object
        :return: python list of databases matching the pattern
        """
        self.logger.info("Getting the databases list")
        if bool(len(ora_config.oracle_db_inclusion_list)):
            self.logger.info("{} Databases found in oracle_db_inclusion_list".format(
                ora_config.oracle_db_inclusion_list))
            if bool(ora_config.oracle_db_exclusion_list):
                self.logger.info("{} Databases found in oracle_db_exclusion_list".format(
                    ora_config.oracle_db_exclusion_list))
            else:
                self.logger.info("No Databases found in oracle_db_exclusion_list")

        else:
            self.logger.info("No Databases found in oracle_db_inclusion_list")
            if bool(ora_config.oracle_db_exclusion_list):
                self.logger.info("{} Databases found in oracle_db_exclusion_list".format(
                    ora_config.oracle_db_exclusion_list))
            else:
                self.logger.info("No Databases found in oracle_db_exclusion_list")

        final_input_list = ['SH', 'ADMIN', 'ME']
        self.logger.debug(ora_config.get_dbs_list_query.format(
            '^{}$'.format('$|^'.join(final_input_list))))
        result = run_oracle_query(conn, ora_config.get_dbs_list_query.format(
            '^{}$'.format('$|^'.join(final_input_list))))
        final_list = list()
        for row in result:
            final_list.append(row[0])
        return final_list

    def get_table_list(self, conn, db):
        """

        :param conn:
        :param db:
        :return:
        """
        self.logger.debug(ora_config.get_tables_list_query.format(db))
        result = run_oracle_query(conn, ora_config.get_tables_list_query.format(db))
        final_list = list()
        for row in result:
            final_list.append(row[0])
        return final_list

    def get_column_details(self, conn, db, table):
        """

        :param conn:
        :param db:
        :param table:
        :return:
        """
        self.logger.debug(ora_config.get_column_list_query.format(table, db))
        result = run_oracle_query(conn, ora_config.get_column_list_query.format(table, db))
        final_list = list()
        for row in result:
            column_data = {
                'COLUMN_NAME': row[0],
                'DATA_TYPE': row[1],
                'DATA_PRECISION': row[2],
                'DATA_SCALE': row[3],
                'DATA_LENGTH' : row[4],
                'NULLABLE': row[5]
            }
            final_list.append(column_data)
        return final_list

    def get_constraint_details(self, conn, db, table):
        self.logger.debug(ora_config.get_pk_constraint_list_query.format(table, db))
        result = run_oracle_query(conn, ora_config.get_pk_constraint_list_query.format(table, db))
        final_list = list()
        for row in result:
            column_data = {
                'CONSTRAINT_NAME': row[0],
                'COLUMN_NAME': row[1]
            }
            final_list.append(column_data)
        result = run_oracle_query(conn, ora_config.get_fk_constraint_list_query.format(table, db))
        final_list = list()
        for row in result:
            column_data = {
                'CONSTRAINT_NAME': row[0],
                'COLUMN_NAME': row[1],
                'FK_TABLE_NAME': row[2],
                'FK_CONSTRAINT_NAME': row[3],
            }
            final_list.append(column_data)
        return final_list
