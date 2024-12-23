import logging
import sys
from . import query
from . import database
from psycopg2.extensions import connection


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger('INFO')


""" This file contains all function to database access"""

@database.db_operator
def get_all_files(connection : connection):

    with connection.cursor() as conn:
        conn.execute(
            query.get_all_files
        )
        return conn.fetchall()

@database.db_operator
def ins_informations_captured(connection: connection, params: dict):

    with connection.cursor() as conn:
        conn.execute(
            query=query.ins_informations_captured, vars=params
        )
    connection.commit()
    logger.info(f"ITEM : {params} adicionado na base de dados !")