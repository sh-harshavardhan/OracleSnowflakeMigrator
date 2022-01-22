# OracleSnowflakeMigrator

### Features
- Extract DDLs from Oracle and store them as JSON.
- Convert JSON DDLs to Snowflake DDLs.
- Deploy the DDLs to Snowflake.

### Next Steps
- Capture schema changes in Oracle, and apply the same is Snowflake.
- Expand the list of datatypes that can be converted from Oracle to Snowflake. Checkout existing [ora_snow_datatype_mapping.py](conf/ora_snow_datatype_mapping.py)
- Create `setup.py` to allow users to install and run the scripts using commands. (Entry points)
- Creation and connecting of Snowflake `stages` to tables.

