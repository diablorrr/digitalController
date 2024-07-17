from flask import Blueprint,Response
from ...tools.sse import SSE,formatSSE
import random,time
from ...tools.paramiko_ssh import paramiko_instance

chatFrameBp = Blueprint("Frame",__name__)

sse = SSE()

@chatFrameBp.route('/api/chat',methods=['POST'])
def test_sse():
    
    paramiko_instance.send_command('ls')
    time.sleep(1)
    output = paramiko_instance.read_output()
    print(output)
    sse.announce(formatSSE(output))
    return 'OK'




@chatFrameBp.route('/api/chat/listen',methods=['GET'])
def test_listen():
    print("test listen")
    def stream():
        messages = sse.listen()
        while True:
            msg = messages.get()
            print(msg)
            time.sleep(0.1)
            yield msg
    return Response(stream(),mimetype="text/event-stream")
