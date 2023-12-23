<<<<<<< HEAD
from src import create_app
from src.config import settings
=======
from website import create_app
>>>>>>> production

app = create_app()

if __name__=='__main__':
<<<<<<< HEAD
    app.run(
        port=settings.port,
        debug=settings.debug
    )
=======
    app.run(debug=True)
>>>>>>> production
