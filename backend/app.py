from flask import Flask,jsonify,request,Response
from flask_cors import CORS
import random
from queue import Queue
from tools.SSE import SSE, formatSSE

app = Flask(__name__)
CORS(app)

q = Queue(maxsize=50)

@app.route('/api/submit',methods=['POST'])
def submit_data():
    if request.method == 'POST':
        request_data = request.data.decode('utf-8')
        print(request_data)
        response_data = {'message':'Data received','data':request_data}
        return jsonify(response_data)
    return ''

sse = SSE()
@app.route('/api/test',methods=['POST'])
def test_sse():
    for _ in range(10):
        sse.announce(formatSSE(str(random.randint(1,10))))
    print(sse.listeners.queue)
    return 'OK' #jsonify(response_data)
    



@app.route('/api/test/listen',methods=['GET'])
def test_listen():
    print("test listen")
    def stream():
        messages = sse.listen()
        while True:
            msg = messages.get()
            print(msg)
            yield msg
    return Response(stream(),mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(debug=True)

