import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from base64 import b64encode
from collections import OrderedDict
from hashlib import sha256
from hmac import HMAC
from urllib.parse import urlparse, parse_qsl, urlencode

#TODO: access database parameters
#TODO: make decorator for vk id validation or just check in each function

client_secret = "fDHsb7dWwsFGqQv9z9Vb"

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User


@app.route('/')
def hello():
    return jsonify({'hello': True})

@app.route('/users/<id>', methods=['GET'])
@cross_origin()
def task_info(id):
    #Debug getting query O(1) difficulty
    users = User.query.filter_by(user_vk_id=id).first()
    print("users:", users)
    referrer = request.headers.get("Referer")
    print("Referrer: ", referrer)
    if referrer:
        query_params = dict(parse_qsl(urlparse(referrer).query, keep_blank_values=True))
        status = is_valid(query=query_params, secret=client_secret)
        print("ok" if status else "fail")
    if users:
        print("User exists")
        result = { "data": {"vk_user_id": id, "status": "old"}}
        return jsonify(result)
    else:
        try:
            new_user = User(user_vk_id = id)
            db.session.add(new_user)
            db.session.commit()
            print("New User Created!")
            result = { "data": {"vk_user_id": id, "status": "new"}}
            return jsonify(result)
        except Exception as e:
            return(str(e))


def is_valid(*, query: dict, secret: str) -> bool:
    """Check VK Apps signature"""
    vk_subset = OrderedDict(sorted(x for x in query.items() if x[0][:3] == "vk_"))
    hash_code = b64encode(HMAC(secret.encode(), urlencode(vk_subset, doseq=True).encode(), sha256).digest())
    decoded_hash_code = hash_code.decode('utf-8')[:-1].replace('+', '-').replace('/', '_')
    return query["sign"] == decoded_hash_code

if __name__ == '__main__':
    app.run()
