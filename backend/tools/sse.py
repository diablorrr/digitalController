from queue import Queue

class SSE:
    def __init__(self):
        self.listeners = Queue(maxsize=100)

    def listen(self):
        return self.listeners

    def announce(self,msg):
        self.listeners.put_nowait(msg)

# 对消息格式化，没json化？？
def formatSSE(data:str) -> str:
    msg = f"data: {data}\n\n"
    return msg
