### SCRIPT EJEMPLO BACKEND CON SERVIDOR WEBSOCKET
# En este script se implementa un servidor para la comunicación mediante websockets de 
# señales de los equipos de prácticas

# La comunicación entre el dispositivo de prácticas y el backend se realiza mediante websocket
# La comunicación entre el backend y el frontend se realiza mediante socket IO (websockets) 


import asyncio
import websockets
from flask import Flask, render_template
from flask_socketio import SocketIO
import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


# Se implementa el root endpoint
@app.route('/')
def index():
    return render_template('index.html')





### Gestión de la entrada de mensajes
async def ws_handler(websocket):
    print("ESP32 conectado")
    try:
        async for message in websocket:
            print(f"[ESP32] → {message}")
            socketio.emit("dato_esp32", {"dato": message})
    except websockets.exceptions.ConnectionClosed:
        print("ESP32 desconectado")

## Inicio del servidor websokets
def iniciar_ws_server():
    async def start_server():
        async with websockets.serve(ws_handler, "0.0.0.0", 8765):
            print("Servidor WebSocket corriendo en puerto 8765")
            await asyncio.Future()  # Mantenerlo corriendo para siempre

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_server())

# Lanzar WebSocket server en hilo separado
ws_thread = threading.Thread(target=iniciar_ws_server)
ws_thread.daemon = True
ws_thread.start()


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000)
