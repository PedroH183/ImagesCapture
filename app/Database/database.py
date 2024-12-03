import psycopg2
from functools import wraps
from psycopg2.extensions import connection
from psycopg2.pool import SimpleConnectionPool
from app.SingletonInterface import SingletonInterface


class PostgresPool(SingletonInterface):

    params = {
        "port" : "7000",
        "user" : "postgres",
        "host" : "0.0.0.0",
        "password" : "1234",
        "database" : "imagecapturedb"
    }

    def __init__(self):
        self.postgres_pool: SimpleConnectionPool = \
            psycopg2.pool.SimpleConnectionPool(1,5, **self.params)

    def get_conn(self):
        return self.postgres_pool.getconn()


def db_operator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        """
            Responsável pela captura de todos os parametros que foram passados 
            para a função e devolver a conexão para a pool.
        """

        conn : connection = None
        try:
            conn = PostgresPool().get_conn()
            return function(conn, *args, **kwargs)

        except Exception as e:
            print(f"Error ao executar uma função no banco :: {str(e)}")
        finally:
            if conn:
                print(f"Termino de execução de operação no banco")

    return wrapper