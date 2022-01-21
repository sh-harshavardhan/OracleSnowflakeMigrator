import conf.oracle_config as ora_config
import cx_Oracle
import logging


class Connection:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_connection(self):
        self.logger.info("Getting the connection object for Oracle")
        cx_Oracle.init_oracle_client(lib_dir=ora_config.oracle_client_dir)
        conn_details = ora_config.oracle_connection_details
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
