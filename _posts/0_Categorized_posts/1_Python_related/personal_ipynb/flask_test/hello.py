


"""
- 간단하게, 그냥 index할 주소, html텍스트를 넘겨주는 함수 이런식으로 세팅된다고 생각하면 될듯 
- flask run 
- 단 자동으로 update해주기 위해서는 다음으로 실행 
$ export FLASK_APP=main.py
$ export FLASK_DEBUG=1
$ flask run

- http://bluese05.tistory.com/44


"""
from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World! page입니다'

## uri에 넘어온 값을 사용 
@app.route('/user/<username>')
def show_username(username):
    return "your name is {}, right?".format(username)
## 입력받는 변수의 데이터 타입을 설정할 수 있음.
## 물론 스트링으로 입력받아서 처리해도 상관없음
@app.route('/user/id/<int:userid>')
def show_user_id(userid):
    return "your id is {}, right?".format(userid)

## 아래처럼 두 개를 겹쳐 놓으면, 두 경우에 대해서 모두 수행됨. 
## 단, 이 경우에 argument의 초기값이 정해져 있는 것을 확인
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', 
    name='\n'.join([name*10 for i in range(0, 20)])
    )

# redirect를 이용해서 제어할 수 있다.
@app.route('/aaa')
def aaa(): 
    return redirect('/')
# uri에 변수가 포함되어 있을 때는, 함수에서도 해당 변수가 선언되어 있어야 함 
@app.route('/draw/<number>')
def draw_start(number):
    r_str = ""
    for i in range(1, int(number)):
        r_str+="*"*i
        r_str+='<br>'# html에서의 줄바꿈으로 해야함 not \n
    return r_str