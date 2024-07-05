from flask import Blueprint,Response
from ..tools.sse import SSE,formatSSE
import random,time

chatFrameBp = Blueprint("Frame",__name__)

sse = SSE()

@chatFrameBp.route('/api/chat',methods=['POST'])
def test_sse():
    for _ in range(100):
        sse.announce(formatSSE(str(random.randint(1,10))))
    print(sse.listeners.queue)
    return 'OK'




@chatFrameBp.route('/api/chat/listen',methods=['GET'])
def test_listen():
    print("test listen")
    def stream():
        messages = sse.listen()
        while True:
            msg = messages.get()
            print(msg)
            time.sleep(1)
            yield msg
    return Response(stream(),mimetype="text/event-stream")
