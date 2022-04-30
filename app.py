from flask import Flask
from api.route.home import home_api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_api, url_prefix='/api')
    return app


if __name__ == "__main__":
    #source /home/patrick/Bureau/python/any_prj/envs/env_rest/bin/activate
    # flask run --port=8000 -h 0.0.0.0

    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8000,
                        type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    print(port)

    app = create_app()

    app.run(host='0.0.0.0', port=port, debug=True)
