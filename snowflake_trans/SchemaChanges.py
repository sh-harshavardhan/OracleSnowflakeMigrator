import glob
import json
import logging
from conf import snowflake_config as snow_conf
from snowflake_trans.Connection import Connection


class SchemaChanges:
    conn_obj = Connection()
    snow_conn = conn_obj.get_connection()

    def __init__(self):
        self.logger = logging.getLogger(__name__)


