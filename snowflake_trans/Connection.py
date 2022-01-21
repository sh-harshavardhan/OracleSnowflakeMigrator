import snowflake.connector
import logging
import conf.snowflake_config as snow_conf


class Connection:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_connection(self):
        conn_details = snow_conf.snowflake_connection_details
        if not bool(conn_details.get("account")):
            self.logger.error("account missing in snowflake_connection_details")
            exit(1)
        if not bool(conn_details.get("username")):
            self.logger.error("username missing in snowflake_connection_details")
            exit(1)
        if not bool(conn_details.get("password")):
            self.logger.error("password missing in snowflake_connection_details")
            exit(1)
        try:
            conn_obj = snowflake.connector.connect(
                user=conn_details.get("username"),
                password=conn_details.get("password"),
                account=conn_details.get("account")
            )
            return conn_obj
        except Exception as e:
            self.logger.error("Failed to connect to snowflake")
            print(e)
            exit(1)
