import werkzeug.serving
from constants import Constants
from controllers.connector import app
from utils.database_utils import DatabaseUtils
from utils.logger import Logger


def run_server():
    DatabaseUtils.init_cluster_db(Constants.DATABASE_URL)
    Logger.log_including_time("waitress_server", "run_server", f"Listening on port {Constants.PORT}")
    werkzeug.run_simple('127.0.0.1', int(Constants.PORT), app, use_debugger=True, use_reloader=True)


if __name__ == '__main__':
    run_server()
