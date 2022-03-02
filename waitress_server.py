from waitress import serve
from constants import Constants
from utils.database_utils import DatabaseUtils
from controllers.connector import app
from utils.logger import Logger
import werkzeug.serving


@werkzeug.serving.run_with_reloader
def run_server():
    DatabaseUtils.init_local_db()
    Logger.log_including_time("waitress_server", "run_server", f"Listening on port {Constants.PORT}")
    serve(app, host='0.0.0.0', port=Constants.PORT)


if __name__ == '__main__':
    run_server()
