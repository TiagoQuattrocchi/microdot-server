from boot import connect_to
from microdot import Microdot, send_file
from machine import Pin
import ds18x20
import onewire
import time

buzzer_pin = Pin(14, Pin.OUT)
ds_pin = Pin(19)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
temperatureCelsius = 0

connect_to()
app = Microdot()

@app.route('/')
async def index(request):
    return send_file('index.html')

@app.route('/<dir>/<file>')
async def static(request, dir, file):
    return send_file(f"{dir}/{file}")

@app.route('/sensors/ds18b20/read')
async def temperature_measuring(request):
    global temperatureCelsius
    ds_sensor.convert_temp()
    time.sleep_ms(750)

    roms = ds_sensor.scan()
    for rom in roms:
        temperatureCelsius = ds_sensor.read_temp(rom)

    return {'temperatura': temperatureCelsius}

@app.route('/setpoint/set/<int:value>')
async def setpoint_calculation(request, value):
    global temperatureCelsius
    print("Calculate setpoint")

    if value >= temperatureCelsius:
        buzzer_pin.on()
        response = {'buzzer': 'Encendido'}
    else:
        buzzer_pin.off()
        response = {'buzzer': 'Apagado'}

    return response

app.run(port=80)