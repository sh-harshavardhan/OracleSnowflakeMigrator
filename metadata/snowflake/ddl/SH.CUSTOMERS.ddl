CREATE OR REPLACE TABLE TEST.SH.CUSTOMERS (
CUST_ID NUMBER ,
CUST_FIRST_NAME VARCHAR ,
CUST_LAST_NAME VARCHAR ,
CUST_GENDER VARCHAR ,
CUST_YEAR_OF_BIRTH NUMBER(4) ,
CUST_MARITAL_STATUS VARCHAR NOT NULL,
CUST_STREET_ADDRESS VARCHAR ,
CUST_POSTAL_CODE VARCHAR ,
CUST_CITY VARCHAR ,
CUST_CITY_ID NUMBER ,
CUST_STATE_PROVINCE VARCHAR ,
CUST_STATE_PROVINCE_ID NUMBER ,
COUNTRY_ID NUMBER ,
CUST_MAIN_PHONE_NUMBER VARCHAR ,
CUST_INCOME_LEVEL VARCHAR NOT NULL,
CUST_CREDIT_LIMIT NUMBER NOT NULL,
CUST_EMAIL VARCHAR NOT NULL,
CUST_TOTAL VARCHAR ,
CUST_TOTAL_ID NUMBER ,
CUST_SRC_ID NUMBER NOT NULL,
CUST_EFF_FROM DATE NOT NULL,
CUST_EFF_TO DATE NOT NULL,
CUST_VALID VARCHAR NOT NULL)