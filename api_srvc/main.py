from flask import Flask
from Router.controller import bp
from database.database import PostgresPool

app = Flask(__name__)
postgres_pool = PostgresPool()

app.register_blueprint(bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)