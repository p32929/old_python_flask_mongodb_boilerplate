from waitress import serve
import server
from constants import Constants

print(f"Listening on port {Constants.PORT}")
serve(server.app, host='0.0.0.0', port=Constants.PORT)
