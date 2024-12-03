from flask import Flask

from app.Database import database
from app.Router.controller import bp

app = Flask(__name__)
postgres_pool = database.PostgresPool()

app.register_blueprint(bp)