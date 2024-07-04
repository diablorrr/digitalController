from queue import Queue

class SSE:
    def __init__(self):
        self.listeners = Queue(maxsize=100)

    def listen(self):
        return self.listeners

    def announce(self,msg):
        self.listeners.put_nowait(msg)

def formatSSE(data:str,event=None) -> str:
    msg = f"data: {data}\n\n"
    if event is not None:
        msg = f"event: {event}\n{msg}"
    return msg
