from dotenv import load_dotenv
import os
import psycopg2


def get_postgres_connection():
    try:
        load_dotenv()
        connection = psycopg2.connect(
        user = os.getenv("DB_USERNAME"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_NAME"),
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT")
        )

        print("Connection established")
        return connection

    except Exception as e:
        print(f"Connection error: {e}")
        return None

def create_table(cursor):
    create_query = """
    CREATE TABLE IF NOT EXISTS customers_table (
        index INTEGER,
        customer_id TEXT,
        first_name TEXT,
        last_name TEXT,
        company TEXT,
        city TEXT,
        country TEXT,
        phone_1 TEXT,
        phone_2 TEXT,
        email TEXT,
        subscription_date TIMESTAMP,
        website TEXT
    );
    """

    cursor.execute(create_query)
    print("Table created successfully")

def insert_data(connection, cursor, df):
    insert_query = """
        INSERT INTO customers_table (
            index, customer_id, first_name, last_name,
            company, city, country, phone_1, phone_2,
            email, subscription_date, website
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    for row in df.itertuples(index=False):
        cursor.execute(insert_query, tuple(row))

    connection.commit()
    print("Data inserted successfully.")
