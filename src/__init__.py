from flask import Flask, jsonify
from flask_caching import Cache
from flask_assets import Environment

from src.config import settings
from src.utils.assets import bundles

cache = Cache()
assets = Environment()

def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)

    app.config['DEBUG'] = settings.debug

    # assets.init_app(app)

    with app.app_context():
        assets.init_app(app)
        cache.init_app(app)

    assets.register(bundles)
    
    @app.route('/healthcheck')
    def healthcheck():
        status = {'status' : 'good'}
        return jsonify(status), 200

    from src.blueprints.views.routes import bp as views_bp
    app.register_blueprint(views_bp)

    return app