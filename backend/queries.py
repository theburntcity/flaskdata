import psycopg2
from backend.config import dbconfig
import os 
 
def onequery():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = dbconfig()
 
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
 
        # create a cursor
        cur = conn.cursor()
        
        # execute a statement
        with open(r"backend\sqlfiles\all.sql", 'r') as f:
            cur.execute(f.read())
        conn.commit()
 
        # return all records
        queryone = cur.fetchall()
       
     # close the PostgreSQL cursor
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            # close the cursor with the PostgreSQL
            cur.close()
            # close the connection with the PostgreSQL
            conn.close()
            print("The database is closed.")
    return queryone


# print(onequery())