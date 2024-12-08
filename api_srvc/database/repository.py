from . import query
from . import database
from psycopg2.extensions import connection

""" This file contains all function to database access"""

@database.db_operator
def get_all_files(connection : connection):

    with connection.cursor() as conn:
        conn.execute(
            query.get_all_files
        )
        return conn.fetchall()