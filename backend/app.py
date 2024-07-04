from flask import Flask,jsonify,request,Response
from flask_cors import CORS
import random
from queue import Queue
from tools.SSE import SSE

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

@app.route('/api/test',methods=['POST'])
def test_sse():
    count = 10
    while count:
        q.put(random.randint(1,10))
        count -= 1
        response_data = {'message':'Data received','data':str(q.queue)}
        return jsonify(response_data)



@app.route('/api/test/listen',methods=['GET'])
def test_listen():
    sse = SSE()
    for _ in range(10):
        sse.listeners.put(random.randint(1,10))
    def stream():
        messages = sse.listen()
        count = 10
        while count:
            msg = messages.get()
            yield msg
            count -= 1
    return Response(stream(),mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(debug=True)

