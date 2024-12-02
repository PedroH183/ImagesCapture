from flask import Flask
from Database.database import PostgresPool

app = Flask(
    "ImagesCaptureRouter"
)
postgres_pool = PostgresPool()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)