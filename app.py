import os
import psycopg2
from flask import Flask
from dotenv import load_dotenv
from auth_blueprint import authentication_blueprint
from hoots_blueprint import hoots_blueprint
from comments_blueprint import comments_blueprint

load_dotenv()

if 'ON_HEROKU' in os.environ:
    connection = psycopg2.connect(
        os.getenv('DATABASE_URL'), 
        sslmode='require'
    )
else:
    connection = psycopg2.connect(
        host='localhost',
        database=os.getenv('POSTGRES_DATABASE'),
        user=os.getenv('POSTGRES_USERNAME'),
        password=os.getenv('POSTGRES_PASSWORD')
    )

app = Flask(__name__)
app.register_blueprint(hoots_blueprint)
app.register_blueprint(authentication_blueprint)
app.register_blueprint(comments_blueprint)

@app.route('/', methods=['GET'])
def signup():
    return "Hello world."

if __name__ == '__main__':
    app.run()
