from flask import Flask, jsonify, g
from src.config import settings
from flask_caching import Cache

cache = Cache()

def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)

    app.config['DEBUG'] = settings.debug

    with app.app_context():
        cache.init_app(app)

    @app.route('/healthcheck')
    def healthcheck():
        status = {'status' : 'good'}
        return jsonify(status), 200

    from src.blueprints.views.routes import bp as views_bp
    app.register_blueprint(views_bp)

    return app
