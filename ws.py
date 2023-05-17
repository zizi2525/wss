from flask import Flask,render_template,request
import requests
from flask_sock import Sock
import asyncio
import websocket
import rel
app = Flask(__name__)
sock =Sock(app)
loop = asyncio.get_event_loop()
from websocket import create_connection
import json


@sock.route('/<path:path>') 
def so(ws,**kwargs):
  
    id = request.args.get('id')
    print(id)
    extra_header=dict(request.headers)
    hos=request.path.replace('/','')
    extra_header.update({"Origin":'https://freeplayervideo.com','Host':hos})

    extra_header ={

 "Origin":"https://freeplayervideo.com",      
"Sec-WebSocket-Key": request.headers["Sec-WebSocket-Key"],
"Sec-WebSocket-Version":  request.headers["Sec-WebSocket-Version"],

"Pragma": "no-cache",
"Cache-Control": "no-cache",
"User-Agent": request.headers["User-Agent"],

"Accept-Encoding": request.headers["Accept-Encoding"],
"Accept-Language": request.headers["Accept-Language"],

"Sec-Websocket-Extensions": request.headers["Sec-Websocket-Extensions"],

    }
   
   
    #wss = websocket.WebSocket()
    
 
    def on_message(wsapp, message):
      
       ws.send(message)
    def on_open(wss):
       wss.send(ws.receive())
       
    def on_ping(wsapp, message):
        print(message)
      

    def on_pong(wsapp, message):
      
      wsapp.send(ws.receive())
    websocket.enableTrace(True)
    wsapp = websocket.WebSocketApp("wss://"+hos,subprotocols=[request.headers["Sec-Websocket-Protocol"]],header=extra_header,on_open=on_open, on_message=on_message, on_ping=on_ping, on_pong=on_pong)
    wsapp.run_forever(origin="https://freeplayervideo.com", host=hos,ping_interval=1, ping_timeout=None, suppress_origin=True)
   
       
     
@sock.route('/e/<path:path>') 
def sos(ws,**kwargs):
 

    extra_header=dict(request.headers)
    hos=request.path.replace('/e/','')
    extra_header.update({"Origin":'https://freeplayervideo.com','Host':hos})
    del extra_header["Upgrade"]
    del extra_header["Origin"]
    print(hos)
    
    extra_header = {


"User-Agent": request.headers['User-Agent'],
"Accept": request.headers['Accept'],
"Accept-Language": request.headers['Accept-Language'],
"Accept-Encoding": request.headers['Accept-Encoding'],
"Sec-WebSocket-Version":str(request.headers['Sec-WebSocket-Version']),

"Sec-WebSocket-Extensions": request.headers['Sec-WebSocket-Extensions'],
"Sec-WebSocket-Key": request.headers['Sec-WebSocket-Key'],
"Sec-WebSocket-Protocol": request.headers['Sec-WebSocket-Protocol'],
"Connection": request.headers['Connection'],
"Sec-Fetch-Dest": request.headers['Sec-Fetch-Dest'],
"Sec-Fetch-Mode": request.headers['Sec-Fetch-Mode'],
"Sec-Fetch-Site": request.headers['Sec-Fetch-Site'],
"Pragma": request.headers['Pragma'],
"Cache-Control": request.headers['Cache-Control'],



}
    extra_header=dict(request.headers)
    headerchrome={
        
 
'Pragma': 'no-cache',
 'Cache-Control': 'no-cache', 
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36', 

   'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7', 
   "Sec-WebSocket-Version":str(request.headers['Sec-WebSocket-Version']),
    
     'Sec-Websocket-Extensions': request.headers['Sec-Websocket-Extensions'], 
     'Sec-Websocket-Protocol': request.headers['Sec-Websocket-Protocol'],  }
    print(request.headers)
    #wss = websocket.WebSocket()
    
    
    def on_message(wsapp, message):
      
       ws.send(message)
    def on_open(wss):
       wss.send(ws.receive())
    def on_ping(wsapp, message):
        print(message)
      

    def on_pong(wsapp, message):
      
      wsapp.send(ws.receive())
    websocket.enableTrace(True)
    wsapp = websocket.WebSocketApp("wss://"+hos,header=headerchrome,on_open=on_open, on_message=on_message, on_ping=on_ping, on_pong=on_pong)
    wsapp.run_forever(origin="https://freeplayervideo.com", host=hos,ping_interval=4, ping_timeout=None,)
   
       
       
 
if __name__ == "__main__":

  app.run(host='0.0.0.0',debug=True, port="8081")