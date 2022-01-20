import conf.oracle_config as ora_config
import cx_Oracle
import logging
import sys


class Connection:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def set_lib_dir(self):
        instant_client_dir = None
        if sys.platform.startswith("win"):
            instant_client_dir = r"C:\oraClient\instantclient_19_9"
        if instant_client_dir is not None:
            cx_Oracle.init_oracle_client(lib_dir=instant_client_dir)

    def get_connection(self):
        self.logger.info("Getting the connection object for Oracle")
        self.set_lib_dir()
        conn_details = ora_config.oracle_connection_details
        if not bool(conn_details.get("server")):
            self.logger.error("server missing in oracle_connection_details")
            exit(1)
        if not bool(conn_details.get("username")):
            self.logger.error("username missing in oracle_connection_details")
            exit(1)
        if not bool(conn_details.get("password")):
            self.logger.error("password missing in oracle_connection_details")
            exit(1)
        if not bool(conn_details.get("service")):
            self.logger.error("service missing in oracle_connection_details")
            exit(1)
        # if not bool(conn_details.get("port")):
        #     self.logger.error("port missing in oracle_connection_details")

        try:
            conn = cx_Oracle.connect(user=conn_details.get("username"),
                                     password=conn_details.get("password"),
                                     # dsn="{}:{}/{}".format(conn_details.get("server"),
                                     #                       conn_details.get("port"),
                                     #                       conn_details.get("service")
                                     #                       ),
                                     dsn=conn_details.get("dsn"),
                                     encoding="UTF-8"
                                     )
            return conn
        except Exception as e:
            self.logger.error("Failed to get a connection to Oracle")
            print(e)
            exit(1)
