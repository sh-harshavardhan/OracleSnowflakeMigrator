"""
This file maps the oracle datatype to snowflake datatype
oracle_datatype : snowflake_datatype
"""

ora_snow_datatype_mapping = {
    "NUMBER": "NUMBER",
    "VARCHAR2": "VARCHAR",
    "NVARCHAR2": "VARCHAR",
    "CHAR": "VARCHAR",
    "NCHAR": "VARCHAR",
    "FLOAT": "FLOAT",
    "DATE": "DATE",
    "TIMESTAMP": "TIMESTAMP",
    "TIMESTAMP WITH TIME ZONE": "TIMESTAMP_TZ",
    "TIMESTAMP WITH LOCAL TIME ZONE": "TIMESTAMP_LTZ",
}
