import psycopg2
from functools import wraps
from psycopg2.pool import SimpleConnectionPool
from SingletonInterface import SingletonInterface
from psycopg2.extensions import Connection


class PostgresPool(SingletonInterface):

    params = {
        "port" : "5432",
        "user" : "postgres",
        "host" : "127.0.0.1",
        "password" : "1234",
        "database" : "ImageCaptureDb"
    }

    def __init__(self):
        self.postgres_pool: SimpleConnectionPool = \
            psycopg2.pool.SimpleConnectionPool(1,5, **self.params)

    def get_conn(self):
        return self.postgres_pool.getconn()


def db_operator(function, postgres_pool_instance):
    @wraps
    def wrapper(*args, **kwargs):
        """
            Responsável pela captura de todos os parametros que foram passados 
            para a função e devolver a conexão para a pool.
        """

        conn : Connection = None
        try:
            conn = postgres_pool_instance.get_conn()
            return function(conn, *args, **kwargs)

        except Exception as e:
            print(f"Error ao executar uma função no banco :: {str(e)}")
        finally:
            if conn:
                print(f"Termino de execução de operação no banco")

    return wrapper