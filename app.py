from flask import Flask 
from container_controller import ContainerController

app = Flask(__name__)

cont_ctrl = ContainerController() # ContainerController 객체

@app.route('/containers')
def all_container():  # GET 요청시 get_all_container 함수 결과값을 리턴
        return cont_ctrl.get_all_containers()