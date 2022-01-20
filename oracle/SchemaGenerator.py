import logging
import conf.oracle_config as ora_config
from oracle.Connection import Connection


def run_oracle_query(conn, query):
    """

    :param conn:
    :return:
    """
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result


class SchemaGenerator:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def generate_schema(self):
        """

        :return:
        """
        conn_obj = Connection()
        conn = conn_obj.get_connection()
        master_details = dict()
        db_list = self.get_databases_list(conn)
        self.logger.info("Below are the list of schemas found ::\n{}".format('\n'.join(db_list)))
        for db in db_list:
            table_list = self.get_table_list(conn, db)
            self.logger.info("Below are the list of table found in schema :: {}\n{}".format(db,
                                                                                            '\n'.join(table_list)))

            for table in table_list:
                master_details['db'] = db
                master_details['table'] = table
                master_details['columns'] = self.get_column_details(conn, table)
                master_details['constraints'] = self.get_constraint_details(conn, table)

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
        result = run_oracle_query(conn, ora_config.get_tables_list_query.format(db))
        final_list = list()
        for row in result:
            final_list.append(row[0])
        return final_list

    def get_column_details(self, conn, table):
        pass

    def get_constraint_details(self, conn, table):
        pass
