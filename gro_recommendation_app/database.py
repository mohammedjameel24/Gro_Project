#python
# Import necessary libraries
import sqlite3
from sqlite3 import Error

def create_connection():
    """
    This function creates a SQLite database connection.
    """
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # creates a database in RAM
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def create_table(conn):
    """
    This function creates a table in the SQLite database.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE recommendations (
                id integer PRIMARY KEY,
                user_id integer NOT NULL,
                product_id integer NOT NULL,
                rating integer,
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (product_id) REFERENCES products (id)
            );
        """)
    except Error as e:
        print(e)

def insert_recommendation(conn, recommendation):
    """
    This function inserts a new recommendation into the recommendations table.
    """
    sql = ''' INSERT INTO recommendations(user_id,product_id,rating)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, recommendation)
    return cur.lastrowid

def select_all_recommendations(conn):
    """
    This function selects all recommendations from the recommendations table.
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM recommendations")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    # create a database connection
    conn = create_connection()

    # create tables
    if conn is not None:
        create_table(conn)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()

