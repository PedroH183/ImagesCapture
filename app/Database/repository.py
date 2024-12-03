from . import query
from .database import PostgresPool, db_operator
from psycopg2.extensions import connection

""" This file contains all function to database access"""

@db_operator
def get_all_files(connection : connection):

    with connection.cursor() as conn:
        conn.execute(
            query.get_all_files
        )
        return conn.fetchall()