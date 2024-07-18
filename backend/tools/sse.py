from queue import Queue

class SSE:
    def __init__(self):
        self.listeners = Queue(maxsize=0)

    def listen(self):
        return self.listeners

    def announce(self,msg):
        msg_list = msg.splitlines()
        for msg in msg_list:
            msg = formatSSE(msg)
            self.listeners.put(msg)

# 对消息格式化，没json化？？
def formatSSE(data:str) -> str:
    msg = f"data: {data}\n\n"
    return msg
