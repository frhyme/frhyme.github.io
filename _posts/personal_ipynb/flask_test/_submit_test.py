from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_url_path='/static')

## GET 방식으로 값을 전달받음. 
## num이라는 이름을 가진 integer variable를 넘겨받는다고 생각하면 됨. 
## 아무 값도 넘겨받지 않는 경우도 있으므로 비어 있는 url도 함께 mapping해주는 것이 필요함
@app.route('/')
def main_get(num=None):
    return render_template('submit_test.html', num=num)

@app.route('/calculate', methods=['POST', 'GET'])
def calculate(num=None):
    ## 어떤 http method를 이용해서 전달받았는지를 아는 것이 필요함
    ## 아래에서 보는 바와 같이 어떤 방식으로 넘어왔느냐에 따라서 읽어들이는 방식이 달라짐
    if request.method == 'POST':
        #temp = request.form['num']
        pass
    elif request.method == 'GET':
        ## 넘겨받은 숫자 
        temp = request.args.get('num')
        temp = int(temp)
        ## 넘겨받은 문자
        temp1 = request.args.get('char1')
        ## 넘겨받은 값을 원래 페이지로 리다이렉트
        return render_template('submit_test.html', num=temp, char1=temp1)
    ## else 로 하지 않은 것은 POST, GET 이외에 다른 method로 넘어왔을 때를 구분하기 위함

if __name__ == '__main__':
    # threaded=True 로 넘기면 multiple plot이 가능해짐
  app.run(debug=True, threaded=True)
