import query
from main import postgres_pool
from Database.database import db_operator
from psycopg2.extensions import connection

""" This file contains all function to database access"""

@db_operator(postgres_pool)
def get_all_files(connection : connection):

    with connection.cursor() as conn:
        conn.execute(
            query.get_all_files
        )
        return conn.fetchall()