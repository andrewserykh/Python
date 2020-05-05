

import websocket
import time
 
ws = websocket.WebSocket()
ws.connect("ws://192.168.4.1:81")
 
i = 0
nrOfMessages = 200
 
while i<nrOfMessages:
    ws.send("$PWPEQ,ZDA,GGA,XFA,XDF,POVER*30")
    result = ws.recv()
    print(result)
    i=i+1
    time.sleep(1)
 
ws.close()