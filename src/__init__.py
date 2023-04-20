from flask import Flask, jsonify, g
from src.config import settings
from flask_caching import Cache

cache = Cache()

def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)

    app.config['DEBUG'] = settings.debug

    # cache = Cache(app)

    with app.app_context():
        pass
        cache.init_app(app)
        # g.cache = cache

    @app.route('/healthcheck')
    def healthcheck():
        status = {'status' : 'good'}
        return jsonify(status), 200

    from src.blueprints.views.routes import bp as views_bp
    app.register_blueprint(views_bp)

    # g.cache = cache
    return app

def _before_request():
    pass