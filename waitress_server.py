from waitress import serve
from constants import Constants
from utils.database_utils import DatabaseUtils
from utils.routes import app

DatabaseUtils.init_local_db()
print(f"Listening on port {Constants.PORT}")
serve(app, host='0.0.0.0', port=Constants.PORT)
