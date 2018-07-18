"""
- 값을 입력받고 그 값에 맞춰서 페이지를 만들어주도록 진행하려고 합니다. 
- 아주 간단하게, 숫자를 입력받으면 그 값만큼의 별을 표시하려고 합니다. 
- 사실 url을 통해서 전달받아도 되는 것이기는 한데, 
- 페이지에서 엑셀 파일 이름을 입력받는 식으로 쓸 수 있지 않을까? 싶어서 사용하기로 했습니다. 
"""

from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__, static_url_path='/static')
 
## 간단한 값을 넘길 때는 아래처럼 post, get간의 차이가 분명하게 드러나지 않음. 
## post는 값을 http 내부에 통합해서 넘긴다면, get의 경우는 url을 통해서 넘긴다고 보는게 좋음
@app.route('/post/<int:num>')
def main_post(num=None):
    return render_template('star_post.html', num=num)
@app.route('/get/<int:num>')
def main_get(num=None):
    return render_template('star_get.html', num=num)
@app.route('/txt')
def read_txt():
    ## flask app을 구동할 때 다음 부분을 추가한 다음에 진행해야함. 
    ## app = Flask(__name__, static_url_path='/static')
    f = open('static/test.txt', 'r')
    ## 단 리턴되는 값이 list형태의 타입일 경우 문제가 발생할 수 있음.
    ## 또한 \n이 아니라 </br>으로 처리해야 이해함
    ## 즉 파일을 읽더라도 이 파일을 담을 html template를 만들어두고, render_template 를 사용하는 것이 더 좋음
    return "</br>".join(f.readlines())
@app.route('/py')
def read_py():
    ## 반드시 static에 있지 않아도 읽을 수는 있음.
    ## 현재 파일과 읽으려는 파일이 같은 경로에 있기 때문에 아래와 같은 방식으로 읽을 수도 있음.
    f = open('hello.py', 'r')
    return "</br>".join(f.readlines())


@app.route('/calculate', methods=['POST', 'GET'])
def calculate(num=None):
    ## 어떤 http method를 이용해서 전달받았는지를 아는 것이 필요함
    ## 만약 이 부분이 없을 경우에는 값이 어떤 방식으로 넘어오는지 알 수 없어서 제대로 읽을 수 없음
    ## 아래에서 보는 바와 같이 어떤 방식으로 넘어왔느냐에 따라서 읽어들이는 방식이 달라짐
    if request.method == 'POST':
        temp = request.form['num']
        return redirect(url_for('main_post',num=temp))
    elif request.method == 'GET':
        temp = request.args.get('num')
        return redirect(url_for('main_get',num=temp))
    ## 다른 http method put 들도 있기 때문에 else가 아닌 elif를 사용함
 
if __name__ == '__main__':
    # threaded=True 로 넘기면 multiple plot이 가능해짐
  app.run(debug=True, threaded=True)
