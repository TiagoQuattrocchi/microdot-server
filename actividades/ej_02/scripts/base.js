document.addEventListener('DOMContentLoaded', () => {
    const fechaElemento = document.getElementById('fecha');
    const fechaActual = new Date(document.lastModified);
    const opcionesFecha = { year: 'numeric', month: 'long', day: 'numeric' };
    fechaElemento.textContent = fechaActual.toLocaleDateString('es-ES', opcionesFecha);
});

function controlLED(led) {
    fetch(`/led/toggle/${led}`);
}

function controlRGB() {
    let red = document.getElementById("redRange").value;
    let green = document.getElementById("greenRange").value;
    let blue = document.getElementById("blueRange").value;

    fetch(`/rgbled/change/${red}/${green}/${blue}`);
}