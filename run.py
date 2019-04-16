from app import app
from config import config

if __name__ == "__main__":
    app.run(config["ip"], threaded=True, debug=True, port=5000)