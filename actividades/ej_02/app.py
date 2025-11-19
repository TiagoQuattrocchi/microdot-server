from microdot import Microdot, send_file
from machine import Pin
from boot import connect_to
import neopixel
import network
from time import sleep


led1 = Pin(32, Pin.OUT, value=0)
led2 = Pin(33, Pin.OUT, value=0)
led3 = Pin(25, Pin.OUT, value=0)

rgb = neopixel.NeoPixel(Pin(27), 4)
for i in range(4):
    rgb[i] = (0, 0, 0)

rgb.write()
connect_to()
app = Microdot()

@app.route('/')
async def index(request):
    return send_file('index.html')

@app.route('/<dir>/<file>')
async def static(request, dir, file):
    return send_file("/{}/{}".format(dir, file))

@app.route('/led/toggle/<led>')
async def led_toggle(request, led):
    global led1, led2, led3
    
    if led == 'LED1':
        led1.value(not led1.value())
    elif led == 'LED2':
        led2.value(not led2.value())
    elif led == 'LED3':
        led3.value(not led3.value())
        
    return {"status":"OK"}

@app.route('/rgbled/change/<int:red>/<int:green>/<int:blue>')
async def rgb_led(request, red, green, blue):
    global rgb
    for pixel in range(4):
        rgb[pixel] = (red, green, blue)
    rgb.write()
    return {"status": "OK"}

app.run(port=80)