from flask import Flask, request
from dotenv import load_dotenv
from src.infra.controllers.actionController import action_blueprint

load_dotenv()
app = Flask(__name__)

app.register_blueprint(action_blueprint)

if __name__ == '__main__':
    app.run(debug=True)