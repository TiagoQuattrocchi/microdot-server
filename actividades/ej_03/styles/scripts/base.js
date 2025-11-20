document.addEventListener('DOMContentLoaded', () => {
    const fechaElemento = document.getElementById('fecha');
    const fechaActual = new Date(document.lastModified);
    const opcionesFecha = { year: 'numeric', month: 'long', day: 'numeric' };
    fechaElemento.textContent = fechaActual.toLocaleDateString('es-ES', opcionesFecha);
});


async function readTemperature() {
    const data = await fetchData('/sensors/ds18b20/read');
    if (data) {
        document.getElementById("mostrar-temperatura").innerText = data.temperatura;
    } else {
        document.getElementById("mostrar-temperatura").innerText = "Error";
    }
}

async function sendSetpoint() {
    const value = Number(document.getElementById("setpoint-slider").value);
    const data = await fetchData(`/setpoint/set/${value}`);
    if (data) {
        document.getElementById("estado-buzzer").innerText = data.buzzer;
    } else {
        document.getElementById("estado-buzzer").innerText = "Error";
    }
}

function updateSetpointValue(value) {
    document.getElementById("setpoint-value").innerText = value;
    sendSetpoint();
}

setInterval(readTemperature, 1000);

readTemperature();

