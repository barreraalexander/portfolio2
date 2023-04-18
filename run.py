from src import create_app
from src.config import settings

app = create_app()

if __name__=='__main__':
    app.run(
        port=settings.port,
        debug=settings.debug
    )
