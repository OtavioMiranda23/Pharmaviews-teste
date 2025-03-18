from flask import Flask
from dotenv import load_dotenv
from src.infra.controllers.ActionController import ActionController
from src.infra.repositories.ActionRepository import ActionRepository
import psycopg2
from flask_cors import CORS

load_dotenv()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}}, supports_credentials=True)

@app.route("/<path:path>", methods=["OPTIONS"])
def handle_options(path):
    response = app.make_response()
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response, 204

@app.after_request
def apply_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:5500"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response

DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "mydatabase"
DB_USER = "postgres"
DB_PASSWORD = "admin"

def get_db_connection():
    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return connection
action_repository = ActionRepository(get_db_connection)
action_controller = ActionController(action_repository)
app.register_blueprint(action_controller.blueprint)




if __name__ == '__main__':
    app.run(debug=True)