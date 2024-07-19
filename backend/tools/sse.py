from queue import Queue
import re

class SSE:
    def __init__(self):
        self.listeners = Queue(maxsize=0)

    def listen(self):
        return self.listeners

    def announce(self,msg):
        msg = remove_ansi_escape_sequences(msg)
        msg_list = msg.splitlines()
        for msg in msg_list:
            msg = formatSSE(msg)
            print(msg)
            self.listeners.put(msg)


def formatSSE(data:str) -> str:
    msg = f"data: {data}\n\n"
    return msg


def remove_ansi_escape_sequences(text):
    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)


if __name__ == '__main__':
    sse = SSE()
    msg = 'fsldflsdjfldsjfldsjfl\nakdfkajfsl\n'
    sse.announce(msg)
