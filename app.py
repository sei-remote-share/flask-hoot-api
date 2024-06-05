from flask import Flask
from dotenv import load_dotenv
from auth_blueprint import authentication_blueprint
from hoots_blueprint import hoots_blueprint
from comments_blueprint import comments_blueprint

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.register_blueprint(hoots_blueprint)
    app.register_blueprint(authentication_blueprint)
    app.register_blueprint(comments_blueprint)

    @app.route('/', methods=['GET'])
    def signup():
        return "Hello world."
    
    print(__name__)

    if __name__ == '__main__':
        app.run()
    else:
        return app

create_app()
