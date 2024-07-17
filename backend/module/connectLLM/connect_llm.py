from flask import Blueprint
from ...tools.paramiko_ssh import paramiko_instance

connectBp = Blueprint("connect_llm",__name__)



@connectBp.route('/api/connect',methods=['GET'])
def connect_llm():
    paramiko_instance.connect()
    print('connected')
    return 'ok_connected'
