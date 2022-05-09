import os
from flask import Flask
from flasgger import Swagger
from api.route.home import home_api
from api.db.db_extensions import db_obj, ma_obj


def create_app():
    app = Flask(__name__)
    app.config['SWAGGER'] = {
        'title': 'NANP API starter test',
        "description": "powered by NANP",
        "version": "1.0",
        'termsOfService': "/api/tos",
    }
    swagger = Swagger(app)
    # basedir = /home/patrick/Bureau/python/any_prj/my_rest_api
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{basedir}/data_test/test.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False

    db_obj.init_app(app=app)
    ma_obj.init_app(app=app)

    app.register_blueprint(home_api, url_prefix='/api')
    return app


if __name__ == "__main__":
    #source /home/patrick/Bureau/python/any_prj/envs/env_rest/bin/activate
    # flask run --port=8000 -h 0.0.0.0 --reload

    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8000,
                        type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()
    # db_obj.create_all()

    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)
    app.logger.error('affichage looger debug')
