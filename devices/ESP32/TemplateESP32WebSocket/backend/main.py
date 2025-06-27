
### SCRIPT EJEMPLO BACKEND CON SERVIDOR WEBSOCKET
# En este script se implementa un servidor para la comunicación mediante websockets de 
# señales de los equipos de prácticas

# La comunicación entre el dispositivo de prácticas y el backend se realiza mediante websocket
# La comunicación entre el backend y el frontend se realiza mediante socket IO (websockets) 

# Para ejecutar la aplicación: uvicorn main:socket_app --host 0.0.0.0 --port 8000 --workers 1 --loop uvloop


import asyncio
import socketio
from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import websockets
import struct
import json
import time

# Crear aplicación FastAPI
app = FastAPI()

#####################################################################################
# Crear servidor Socket.IO
#####################################################################################
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
socket_app = socketio.ASGIApp(sio, other_asgi_app=app)

#####################################################################################
# Templates
#####################################################################################
# Montar carpeta de templates (para frontend)
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


#####################################################################################
# Endpoints
#####################################################################################
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


#####################################################################################
# Mensajes recibidos del frontend
#####################################################################################

@sio.event
async def freq_change(sid, data):
    print(f"[FRONTEND] Mensaje recibido: {data['value']}")
    freq_event = {"freq":data['value']}
    conn = [conn for conn in esp32_websockets]
    await conn[0].send(json.dumps(freq_event))
    # emviar el dato recibido por websockets al ESP32


@sio.event
async def Tm_change(sid, data):
    print(f"[FRONTEND] Mensaje recibido: {data['value']}")
    freq_event = {"Tm":data['value']}
    conn = [conn for conn in esp32_websockets]
    await conn[0].send(json.dumps(freq_event))
    # emviar el dato recibido por websockets al ESP32


#####################################################################################
## Gestión de la conexión con el ESP32
#####################################################################################

# Guardar el estado del ESP32 (si necesitas enviarle datos)
esp32_websockets = set()

# Handler de mensajes WebSocket
async def ws_esp32_handler(websocket):
    print("ESP32 conectado")
    esp32_websockets.add(websocket)
    try:
        async for message in websocket:
            if isinstance(message,bytes):
                dataBloc = struct.unpack("<ff",message)
                print(f"[ESP32] → {time.time()}:{dataBloc}")
                await sio.emit("dato_esp32", {"dato": dataBloc[0]})
    except websockets.exceptions.ConnectionClosedError:
        print("ESP32 desconectado")
    finally:
        esp32_websockets.remove(websocket)

# Iniciar WebSocket Server como tarea background
@app.on_event("startup")
async def start_ws_server():
    async def serve_ws():
        async with websockets.serve(ws_esp32_handler, "0.0.0.0", 8765) as server:
            print("Servidor WebSocket corriendo en puerto 8765")
            await server.serve_forever()  # Nunca termina

    asyncio.create_task(serve_ws())