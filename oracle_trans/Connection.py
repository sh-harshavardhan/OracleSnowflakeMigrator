import conf.oracle_config as ora_conf
import cx_Oracle
import logging


class Connection:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_connection(self):
        """
        :Description : To get connection to Oracle
        :return: oracle connection object
        """
        self.logger.info("Getting the connection object for Oracle")
        cx_Oracle.init_oracle_client(lib_dir=ora_conf.oracle_client_dir)
        conn_details = ora_conf.oracle_connection_details
        if not bool(conn_details.get("dsn")):
            self.logger.error("dsn missing in oracle_connection_details")
            exit(1)
        if not bool(conn_details.get("username")):
            self.logger.error("username missing in oracle_connection_details")
            exit(1)
        if not bool(conn_details.get("password")):
            self.logger.error("password missing in oracle_connection_details")
            exit(1)
        # if not bool(conn_details.get("service")):
        #     self.logger.error("service missing in oracle_connection_details")
        #     exit(1)
        # if not bool(conn_details.get("port")):
        #     self.logger.error("port missing in oracle_connection_details")

        try:
            conn = cx_Oracle.connect(user=conn_details.get("username"),
                                     password=conn_details.get("password"),
                                     dsn=conn_details.get("dsn"),
                                     encoding="UTF-8"
                                     )
            return conn
        except Exception as e:
            self.logger.error("Failed to get a connection to Oracle")
            print(e)
            exit(1)

    def run_oracle_query(self,conn, query, failure_exit_flag=True):
        """
        :Description : To run the Query on Oracle
        :param failure_exit_flag: flag to indicate wheather to exit incase of failure
        :param query: Oracle query to be executed
        :param conn: Connection object to Oracle
        :return: results from oracle
        """
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            if failure_exit_flag:
                self.logger.error("Failed to Execute the query on Oracle :: \n{}".format(query))
                exit(1)
            else:
                self.logger.warning("Failed to Execute the query on Oracle :: \n{}".format(query))
