from flask import Flask, jsonify
from src.config import settings

def create_app():
    app = Flask(__name__)

    app.config.from_object(settings)

    app.config['DEBUG'] = settings.debug

    @app.route('/healthcheck')
    def healthcheck():
        status = {'status' : 'good'}
        return jsonify(status), 200

    return app