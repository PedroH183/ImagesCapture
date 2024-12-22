from functools import wraps
from psycopg2 import connect
from psycopg2.extensions import connection
from utils.Singleton import SingletonInterface

# System debug
import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger('INFO')


class PostgreConn:
    """
        A Pool of connection to paralel database access
    """

    __metaclass__ = SingletonInterface

    params = {
        "port" : "5432",
        "user" : "postgres",
        "host" : "db",
        "password" : "1234",
        "dbname" : "imagecapturedb"
    }

    def __init__(self):
        self.connection: connection = connect(**self.params)

    def get_conn(self):
        return self.connection.getconn()


def db_operator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):

        conn : connection = None
        try:
            conn = PostgreConn().connection
            return function(conn, *args, **kwargs)

        except Exception as e:
            logger.info(f"Error ao executar uma função no banco :: {str(e)}")
        finally:
            logger.info(f"Termino de execução de operação no banco")

    return wrapper