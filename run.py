import logging
from datetime import datetime
from config import config

from app import app
from config import config

if __name__ == "__main__":
    if config["logger"]:
        logging.basicConfig(filename='./logs/{}.log'.format(datetime.now().strftime("%Y-%m-%d %H-%M")), level=logging.DEBUG)
    app.run(config["ip"], threaded=True, debug=True, port=5000)
