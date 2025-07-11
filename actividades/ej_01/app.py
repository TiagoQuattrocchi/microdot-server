from microdot import Microdot, Response
import network
from time import sleep

def connect_wifi(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    if not sta_if.isconnected():
        print('Conectando a la red...')
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            print(".", end="")
            sleep(0.5)
    print('Configuración de red:', sta_if.ifconfig())
    return sta_if.ifconfig()[0] 

WIFI_SSID = "Cooperadora Alumnos"
WIFI_PASSWORD = ""

try:
    ip = connect_wifi(WIFI_SSID, WIFI_PASSWORD)
except Exception as e:
    print("error", e)

app = Microdot()
Response.default_content_type = 'text/html'

@app.route('/')
def index(request):
    with open('index.html', 'r') as file:
        html = file.read()
        
    variables = {
        '{{#}}': "Actividad 1",
        '{{Mensaje}}': "Tiago Server",
        '{{Alumno}}': "T"
    }
    
    for placeholder, valor in variables.items():
        html = html.replace(placeholder, valor)
    return html

@app.route('/styles/base.css')
def serve_css(request):
    with open('styles/base.css', 'r') as f:
        return f.read(), 200, {'Content-Type': 'text/css'}

@app.route('/scripts/base.js')
def serve_js(request):
    with open('scripts/base.js', 'r') as f:
        return f.read(), 200, {'Content-Type': 'application/javascript'}
app.run(host=ip, port=80, debug=True)
