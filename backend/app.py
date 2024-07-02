from flask import Flask,jsonify,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/submit',methods=['POST'])
def submit_data():
    if request.method == 'POST':
        request_data = request.data.decode('utf-8')
        print(request_data)
        response_data = {'message':'Data received','data':request_data}
        return jsonify(response_data)



if __name__ == '__main__':
    app.run(debug=True)

