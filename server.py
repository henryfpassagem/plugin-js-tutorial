import flask
from device import Device

device = Device()
app = flask.Flask(__name__)

@app.route('/')
def main():
    return 'Hello World'

@app.route('/get_voltage')
def get_voltage():
    return str(device.voltage)

@app.route('/set_voltage/<new_voltage>')
def set_voltage(new_voltage):
    device.voltage = float(new_voltage)
    return str(device.voltage)

@app.route('/get_current')
def get_current():
    return str(device.current)

@app.route('/set_current/<new_current>')
def set_current(new_current):
    device.current = float(new_current)
    return str(device.current)

@app.route('/resistance')
def resistance():
    return str(device.resistance)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
