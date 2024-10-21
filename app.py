from flask import Flask , jsonify
import random
from flask_autoindex import AutoIndex
app = Flask(__name__)

ppath = "./"

AutoIndex(app, browse_root=ppath)

@app.route('/flag')
def random_fact():
    fact = random.choice(space_facts)
    return jsonify({'flag': 'SAS{g1t_folder_is_s0_sw33t'})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=34678)
