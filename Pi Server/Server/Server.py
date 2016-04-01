from flask import Flask
from flask_socketio import SocketIO
from logging.handlers import RotatingFileHandler
import Constants
import logging, os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def index():
    return 'Hello World'

@app.before_first_request
def initialSetup():
    if Constants.ENABLE_FLASK_LOGGING:
        formatter = logging.Formatter(
            Constants.LOG_FORMAT_FLASK)
        handler = RotatingFileHandler(os.path.join(Constants.LOG_LOCATION_FLASK,Constants.LOG_FILENAME_FLASK), maxBytes=10000000, backupCount=5)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        app.logger.addHandler(handler)
    import Bonjour
    service = Bonjour.Bonjour()
    service.publish()


if __name__ == '__main__':

    socketio.run(app,
                 debug=Constants.ENABLE_FLASK_DEBUG_MODE,
                 host=Constants.SERVER_IP,
                 port=Constants.SERVER_PORT)
