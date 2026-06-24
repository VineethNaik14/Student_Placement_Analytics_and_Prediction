import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="placement_db",
        user="postgres",
        password="bankaisql123",
        port="5432",
    )
