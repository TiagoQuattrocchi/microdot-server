def connect_to():
    import network
    from time import sleep
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    if not sta_if.isconnected():
        print('Conectando a la red...')
        sta_if.connect("Cooperadora Alumnos", "")
        while not sta_if.isconnected():
            print(".", end="")
            sleep(0.5)
    print('Configuración de red:', sta_if.ifconfig())
    return sta_if.ifconfig()[0]