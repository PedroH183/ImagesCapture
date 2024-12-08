from functools import wraps
from psycopg2.extensions import connection
from psycopg2.pool import SimpleConnectionPool
from SingletonInterface import SingletonInterface

# System debug
import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger('INFO')


class PostgresPool(SingletonInterface):
    """
        A Pool of connection to paralel database access
    """

    params = {
        "port" : "5432",
        "user" : "postgres",
        "host" : "db",
        "password" : "1234",
        "dbname" : "imagecapturedb"
    }

    def __init__(self):
        self.postgres_pool: SimpleConnectionPool = SimpleConnectionPool(1,5, **self.params)

    def get_conn(self):
        logger.info("[INFO] ::: TAKING A CONNECTION FROM POOL")
        return self.postgres_pool.getconn()

    def put_conn(self, conn):
        logger.info("[INFO] ::: RETURNS A CONN TO POOL")
        self.postgres_pool.putconn(conn)

    def close_all_connection(self) -> None:
        logger.info("[INFO] ::: CLOSING ALL CONNECTIONS")
        self.postgres_pool.closeall()


def db_operator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):

        conn : connection = None
        try:
            conn = PostgresPool().get_conn()
            return function(conn, *args, **kwargs)

        except Exception as e:
            logger.info(f"Error ao executar uma função no banco :: {str(e)}")
        finally:
            if conn:
                PostgresPool().put_conn(conn)
            logger.info(f"Termino de execução de operação no banco")

    return wrapper