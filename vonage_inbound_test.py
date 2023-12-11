from pprint import pprint
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhooks/inbound-sms', methods=['GET', 'POST'])
def inbound_sms():
    print('inbound_sms 실행됨')
    if request.is_json:
        pprint(request.get_json())
    else:
        data = dict(request.form) or dict(request.args)
        pprint(data)

    return ('', 204)

app.run(port=3000)