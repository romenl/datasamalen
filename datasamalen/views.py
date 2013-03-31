from flask import render_template, Blueprint, jsonify, request
from datasamalen import app
from datasamalen.models import Device
#from datasamalen.mock_data import create_device

devices = Blueprint('devices', __name__, template_folder='templates')


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/json', methods = ['GET'])
def api_root():
    if request.method == 'GET':
        devices = Device.objects.all().order_by('-_id')[:10]

        devices_data = {}
        for d in devices:
            id = str(d.id)

            devices_data[d.mac] = {'power':d.power,'angel':d.angel,'bssid':d.bssid, 'id':id}

        resp = jsonify(devices_data)
        resp.status_code = 200

        return resp