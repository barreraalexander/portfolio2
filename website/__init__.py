from flask import Flask

def create_app():
    app = Flask(__name__)


    from website.blueprints.main.routes import router

    app.register_blueprint(router)
    # app.config.from_object()

    # assets.init_app(app)
    # assets.register(bundles)

    return app