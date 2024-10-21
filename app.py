from flask import Flask , jsonify
import random
from flask_autoindex import AutoIndex
app = Flask(__name__)

ppath = "./"

AutoIndex(app, browse_root=ppath)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=34678)
