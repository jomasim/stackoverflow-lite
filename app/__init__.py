from app.routes import app
from app.db_config import DBconnection

if __name__ == '__main__':
    app.run(debug=True)
