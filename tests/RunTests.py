from oracle_trans.Connection import Connection

conn = Connection()


get_pk_constraint_list_query = """SELECT a.constraint_name, a.column_name, 
       c_pk.table_name r_table_name,  b.column_name r_column_name
  FROM ALL_CONS_COLUMNS a
  JOIN ALL_CONSTRAINTS c ON a.owner = c.owner
       AND a.constraint_name = c.constraint_name
  JOIN ALL_CONSTRAINTS c_pk ON c.r_owner = c_pk.owner
       AND c.r_constraint_name = c_pk.constraint_name
  JOIN ALL_CONS_COLUMNS b ON C_PK.owner = b.owner
       AND  C_PK.CONSTRAINT_NAME = b.constraint_name AND b.POSITION = a.POSITION     
 WHERE c.constraint_type = 'R'
 and a.TABLE_NAME = 'SALES' AND a.OWNER = 'SH'
 """
results = conn.run_oracle_query(conn.get_connection(), get_pk_constraint_list_query)

for row in results:
    print(row)
