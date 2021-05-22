import asyncio
import pathlib
import ssl
import websocket
import _thread as thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
		for i in range(3):
            time.sleep(1)
			ws.send(100)
    thread.start_new_thread(run, ())

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.5g.schsolution.cz/",
                              on_open = on_open,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)

    ws.run_forever()
	
	