---
title: bokeh로 그림을 그려 봅시다.
category: python-libs
tags: python python-libs bokeh data-visualization
---

## matplotlib이 있는데 왜 bokeh를 써야 하나요? 

- 뭐, 맞는 말씀입니다. 필요하면, matplotlib로 그림을 그리고, 웹으로 내보내야 한다면, `svg`파일로 내보내고 그걸 가져오는 식으로 진행하면 되는데, 굳이 익숙한 matplotlib을 사용하지 않고, 새로운 라이브러리를 배울 필요성이 있나요? 
- 맞습니다. 사실 간단한 그림이라면 굳이 다른 라이브러리를 쓸 필요없이, matplotlib을 가지고도 뭘 많이 할 수 있습니다. 
- 그런데, 사실 그냥 이미지를 웹에 가져와서 띄우는 방식이면, 모양이 생각만큼 예쁘게 나오지는 않습니다(물론 svg라면 일단 화질측면에서는 문제가 없기는 합니다만). 
- 그런데, 사람의 욕심은 끝이 없기 때문에 가능하면 좀더 웹에서 시각적으로 예쁘게 보이도록하고, 마우스를 올리거나 했을때 더 예쁘게 올려지거나 하는 것을 소망하고 있습니다. 그걸 위해서라면 web에서 잘 작동할 수 있도록, javascript등을 이용해서 만드는 것이 더 좋을 것으로 느껴지기도 하구요. 
- 그래서 좀 찾던 와중에 bokeh를 이용하면 이 부분이 꽤 많이, 그리고 편하게 해결되는 것으로 보입니다. 그래서 사용해보려고 해요.

## what is bokeh?? 

- [Bokeh Documentation](https://bokeh.pydata.org/en/latest/)에 따르면, 다음과 같다고 합니다 .

> Bokeh is an interactive visualization library that targets modern web browsers for presentation. Its goal is to provide elegant, concise construction of versatile graphics, and to extend this capability with high-performance interactivity over very large or streaming datasets. Bokeh can help anyone who would like to quickly and easily create interactive plots, dashboards, and data applications.

- 정리하자면, 상호작용이 가능한(interactive) 시각화 라이브러리이며, 특히, 웹브라우저에 특화되어 있다고 할 수 있습니다. interactive plot, dashboard, data application 등을 만들려는 사람들에게 특히 유용할 것이다, 라고 하네요. 
- 그렇습니다. 제가 만들려고 하는 것도 일종의 dashboard입니다. 그래서 bokeh가 좋은 선택안 중 하나가 될것 같습니다. 

### install it. 

- 뭐 길게 생각할 필요없이 우선, 설치부터 합시다. 이렇게 설치를 하면, 필요한 모든 dependency가 모드 함께 설치됩니다. 

```bash
conda install bokeh 
```

## 써봅시다. 

- 말이 길었습니다. 어쨌든, 어떻게 그릴 수 있는지를 그리면 좋겠죠. 그래서 아주 간단한 테스트를 몇 개 해봅니다. 
- 앞서 말씀드린 바와 같이, 그림을 그린 다음 png, svg 등만으로 뽑을 수 있는 것이 아니고, html로 뽑을 수도 있습니다. 그런데, 그걸 현재의 포스트에 모두 작성하는 것은 매우 귀찮고 성가신 일이고, 그림 하나 확인하려고 계속 html로 그림을 확인하는 것은 비효율적이므로 저는 jupyter notebook에서 그림을 확인하면서 진행해보기로 합니다. 

### plot line

- 아래 코드를 쥬피터 노트북에서 치면, 노트북 위에서 그림이 띄워집니다. 
- 언뜻 보기에는 matplotlib과 매우 유사해 보입니다. 단 plot이 아니라 line으로 선을 그린다는 것, figure의 method로서 그림을 그린다는 것 정도가 차이로 보이네요. 

```python
!pip install bokeh

from bokeh.plotting import figure
from bokeh.io import output_notebook, show
# notebook에서 보기 위해서 다음처럼 한 줄을 추가해줍니다.
output_notebook()

# figure를 만들어줍니다. 
# matplotlib의 경우는 figure를 그리고 .xlabel, title 등으로 추가해줬는데, 여기서는 바로 할 수 있네요. 
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

x = [1,2,3,4]
y1, y2 = [4,3,2,1], [1,2,3,4]

# line으로 그려줍니다. 
# matplotlib과 비슷하게 그릴때 관련된 값들을 한번에 넘겨줍니다. 
p.line(x, y1, legend="Y1", line_width=5, line_color='blue')
p.line(x, y2, legend="Y2", line_width=2, line_color='red')

show(p)
```

- circle, rectangle, line, step, multiline, vbars, hbars 등등 매우 다양한 plotting 방법들이 존재합니다. 이걸 하나하나 볼 필요는 없습니다. 그저, 어떤 그림이든 그리려면 웬만한 건 다 그릴 수 있다, 라고 생각하고 필요할때 검색하는 것이 제일 좋은 것 같네요. 

## 그린 것을 뽑아내 봅시다. 

- 그리는 건 대충 해봤습니다. `matplotlib`와 비교하면 아직은 낯설지만, 대략 비슷한 인터페이스를 가지고 있는 것 같습니다. 
- 자 그럼, 됐고, 이제 그린 것을 어떻게 뽑아낼 수 있는지 확인해보려고 합니다. 이게 더 중요하죠. 
- 대략 다음과 같은 방법들이 있을 수 있겠죠. 

### svg 등 이미지로 뽑기 

- svg로 뽑아보려고 합니다. 
- documentation을 보니까 다음처럼 하면 된다고 하네요. 
    - `p.output_backend = "svg"`: 출력방식을 변경하고, 
    - `export_svg(p, filename="plot.svg")`: 로 추출합니다. 

```python
from bokeh.plotting import figure
from bokeh.io import export_svgs,  show

# figure를 만들어줍니다. 
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

x = [1,2,3,4]
y1, y2 = [4,3,2,1], [1,2,3,4]

# line으로 그려줍니다. 
p.line(x, y1, legend="Y1", line_width=5, line_color='blue')
p.line(x, y2, legend="Y2", line_width=2, line_color='red')

######################
## svg로 뽑아줍시다. 
p.output_backend = "svg"
export_svgs(p, filename="plot.svg")
```

- 실행했는데, 다음과 같은 오류가 뜹니다. `PhantomJS`를 설치하라고 합니다.

```
RuntimeError: PhantomJS is not present in PATH or BOKEH_PHANTOMJS_PATH. Try "conda install phantomjs" or             "npm install -g phantomjs-prebuilt"

```

- 영혼없이, 그냥 설치하고 진행하고 싶지만, 예의상 얘가 어떤 놈인지는 한번 알아보도록 합니다. 

#### side: What is PhantomJS?

- [PhantomJS 공식홈페이지의 설명에 따르면 다음과 같다고 합니다. ](http://phantomjs.org/)

> PhantomJS is a headless web browser scriptable with JavaScript. It runs on Windows, macOS, Linux, and FreeBSD. Using QtWebKit as the back-end, it offers fast and native support for various web standards: DOM handling, CSS selector, JSON, Canvas, and SVG.

- 뭐 대충 보면, javascript로 scriptable할 수 있는 headless web browser라고 합니다. headless web browser는 GUI가 없는 웹브라우저를 말하죠. 즉, javascript언어로 웹서핑을 하면서 이런저런 짓을 할 수 있다는 얘기인 것 같네요. 
- 이는 공식 홈페이지에 예제로 나와있는 코드를 보면 더 명확해집니다. 

> The following simple script for PhantomJS loads Google homepage, waits a bit, and then captures it to an image.

- 즉, 아래코드는 PhantomJS가 구글 홈페이지에 접속해서 로드한 다음, 잠시 멈추었다가, 스크린샷을 만드는 코드를 의미합니다. 이런식으로 웹 자동화를 가능하게 한다는 이야기겠죠. 

```javascript
var page = require('webpage').create();
page.open('http://www.google.com', function() {
    setTimeout(function() {
        page.render('google.png');
        phantom.exit();
    }, 200);
});

```

- 이를 정리해서 보면, bokeh에서 이미지를 svg 등의 형식으로 추출할 때 PhantomJS가 필요한 이유는 bokeh로 인해서 만들어진 웹페이지를 스크린샷뜨는데, bokeh가 필요하기 때문이 아닌가 싶습니다. 
- 이제 이해했으니 설치하기로 합니다. 

#### back to export SVG

- 자 일단 PhantomJS를 설치합니다. 보통 javascript의 library를 설치할때는 npm 명령어를 사용하는데, 여기서는 `conda install`로도 설치할 수 있다는 것이 꽤 신기하군요.

```bash
conda install phantomjs
```

- 설치이후에 다시 코드를 실행하면 잘 됩니다 하하핫. 

### html 페이지로 뽑아내기 

- 자, 이제 html 페이지로 직접 뽑아보겠습니다. 이게 더 익숙한 방식이죠.
- 다음처럼 flask를 이용해서 특정 URL에 대해 html을 보내주는 마이크로서버를 만들었습니다. 

```python
@app.route('/bokeh_standalone_HTML')
def bokeh_standalone_HTML():
    from bokeh.plotting import figure
    from bokeh.resources import CDN
    from bokeh.embed import file_html

    plot = figure()
    plot.circle([1,2, 5], [3,4, 8], size=20, color="navy", alpha=0.5)
    plot1 = figure()
    plot1.circle([1,2, 5], [3,4, 8], size=20, color="navy", alpha=0.5)
    """
    - models: 어떤 figure를 그릴지 전달합니다. 2개를 전달하면, 연속으로 하나씩 포함되어서 그려지죠. 
    - resources: resource, 즉 Bokeh JS와 CSS assets들을 가져옵니다. 
    - title: html 내의 태그 중에서 <title>에 해당하는 것을 의미합니다. 
    """
    return file_html(models=[plot, plot1], resources=CDN, title="my plot")
```

- 위를 구현하면, 알아서 잘 웹페이지가 뜨는 것을 알 수 있습니다. 물론, 현재로서는 그냥 그림만 있습니다. 글도 하나도 안 들어가 있고, 그림만 들어가 있어서 영 별로지만, 더 잘할 수 있는 방법은 나중에 고민하도록 합니다. 


### json으로 뽑고 html로 그려주기

- html뿐만 아니라 json으로 뽑을 수도 있습니다. 사실, 그림이 어떻게 JSON으로 변환되는지, 된다면 어떠한 방식인지에 대해서는 제가 잘 모르겠습니다. 나중에 좀 정리해야 할것 같아요. 
- 아무튼 json으로 뽑아낼 수 있는 것 같습니다. 또한 이렇게 뽑아내면, 이 요소를 html 문서 내의 특정 부분에 script로서 집어넣어서, 처리할 수 있을 것으로 보여요. 
- 아무튼 해봅시다. 코드로 보는게 제일 좋죠. 
- 다음처럼 그림을 그리고, 해당 그림 개체를 json 형식의 스트링으로 변경한다음 리턴해주는 함수를 만듭니다. 해당 Url인 `bokeh_json_item`으로 접속을 하면, 그냥 json 형식의 스트링만 뜨게 됩니다. 

```python
@app.route('/bokeh_json_item')
def bokeh_json_item():
    from bokeh.plotting import figure
    from bokeh.embed import json_item
    # figure를 만들고 
    p = figure() 
    # 그림을그리고
    p.circle([1,2, 5], [3,4, 8], size=20, color="navy", alpha=0.5)
    ## 해당 개체를 json형식의 dictionary로 변경해줍니다. 
    jsonified_p = json_item(model=p, target="myplot")
    # json.loads 는 json으로 된 string을 dictionary로 변경해주는 것이고 
    # json.dumps 는 dictionary를 json형식의 string으로 변경해주는 것이죠. 
    return json.dumps(jsonified_p, ensure_ascii=False, indent='\t')
```

- 자, 이제 그림 개체를 json으로 변경해주는 마이크로서버를 만들었다면, 이제 해당 json부분을 받아서, html 페이지에 합쳐서 html 페이지를 그려주는 아이를 만들면 좋겠죠! 해봅니다. 
- 아래처럼 html 페이지를 만듭니다. 중간에 script로 되어 있는 부분에 저희가 앞서 만든 url이 들어갔죠. 이 스크립트에서 필요할 때 해당 url로 접속해서 그림과 관련된 json을 가져오고, Bokeh에서 그림을 그리는 것 같습니다. 

```html
<html>
    <head>

    </head>
    <body>
        <h1>This is h1</h1>
        <script>
            fetch('/bokeh_json_item')
                .then(function(response) { return response.json(); })
                .then(function(item) { Bokeh.embed.embed_item(item); })
        </script>
    </body>
</html>

```

- 그리고, 이제 해당 웹페이지를 뿌려주는 추가 마이크로서버를 하나 더 만듭니다. 이 아이는 그냥, `/bokeh_with_json`로 접속되면, `bokeh_with_json.html`을 뿌려주는 아이일 뿐입니다. 

```python
@app.route('/bokeh_with_json')
def bokeh_with_json():
    return render_template('bokeh_with_json.html')
```

- 그 다음 `bokeh_with_json`에 접속을 햇는데, 글만 뜨고 그림이 안 뜨네요 흠...왜 그럴까요. 
- 생각을 해봅시다. 이전에 SVG를 뽑을 때나, HTML을 뽑을 때는 모두 python 위에서 수행되었습니다. 즉 `import bokeh`로 모두 수행되었다는 이야기죠.
- 그런데, 지금은 script에서 그림이 그려집니다. 즉, script에서 bokeh관련 라이브러리를 인식해야 그림이 그려지지, 이게 없으면 그림이 안 그려진다는 이야기겠죠. 그래서 CDN으로 부터 bokeh를 가져오는 다음 몇 줄을 추가합니다. 

```html
<link rel="stylesheet" href="https://cdn.pydata.org/bokeh/release/bokeh-1.0.4.min.css" type="text/css" />
<script type="text/javascript" src="https://cdn.pydata.org/bokeh/release/bokeh-1.0.4.min.js"></script>
```

- 그런데도 안 그려집니다. 흠. html 코드를 다시 봅시다. 지금은 script만 있는 것을 알 수 있습니다. script는 눈에 보이는 것이 아니고, 뒤에서 일을 처리해주는 아이라고 보면 됩니다. 즉, 뒤에서 돌아가니까 앞에서는 안 보이는 것이죠. 
- 그래서 이럴때는 script의 결과가 표현되는 `div`를 하나 추가해줘야 합니다. 중요하니까 말하면, 항상 **script와 div는 함께 있어야 합니다. 한 놈만 있으면 제대로 그려지지 못합니다**
- 아까 json으로 변환해줄 때, 값을 `target="myplot"`라는 부분이 있었습니다. 이는 저희가 만든 그림 개체의 id가 `'myplot'`라는 것을 의미하죠. 즉 저희가 만들 div의 id가 myplot이라는 의미입니다. 
- 이렇게 다 합쳐진 html 파일은 다음과 같습니다. 이제 잘 되네요 하하핫.

```html
<html>
    <head>
        <link rel="stylesheet" href="https://cdn.pydata.org/bokeh/release/bokeh-1.0.4.min.css" type="text/css" />
        <script type="text/javascript" src="https://cdn.pydata.org/bokeh/release/bokeh-1.0.4.min.js"></script>
        
    </head>
    <body>
        <h1>This is h1</h1>
        <!--
            그림이 그려지는 위치
        -->
        <div id="myplot"></div>
        <!--
            그림을 그려주는 함수, 라이브러리. 
        -->
        <script>
        fetch('/bokeh_json_item').then(function(response) { return response.json(); }).then(function(item) { Bokeh.embed.embed_item(item); })
        </script>
    </body>
</html>

```

### html 페이지에 특정 부분만 그림으로 넣어서 뽑기

- 앞서 봤던 json으로 처리하는 방식과 유사한데, 좀 더 편하게 해줍시다. 
- flask에서는 jinja template engine을 이용해서 특정 부분을 함께 넘겨줘서 렌더링해서 띄울수 있습니다. 
- 예를 들어서, 다음처럼 html template을 만들어준 다음,

```html
<html>
    <head>
        <link rel="stylesheet" href="https://cdn.pydata.org/bokeh/release/bokeh-1.0.4.min.css" type="text/css" />
        <script type="text/javascript" src="https://cdn.pydata.org/bokeh/release/bokeh-1.0.4.min.js"></script>
        
    </head>
    <body>
        <h1>This is h1</h1>
        {% raw %} {{ plot1_div }} {% endraw %} 
        {% raw %} {{ plot1_script }} {% endraw %} 
    </body>
</html>
```

- 다음처럼 html 페이지를 렌더링하면 앞서, html 페이지의 변수부분이 아래처럼 바뀌어서 수행됩니다.
- 이처럼 script, div 부분을 비워둔 다음, 이 부분만 넘겨주면 되는 것 아닐까요? 

```python
@app.route('/plot_template')
def plot_template():
    return render_template('plot_template.html', plot1_div="aaaaa", plot1_script='bbbbb')
```

- 다음처럼 해봅니다. 그러나, 생각처럼 되지 않습니다. 
- script, div가 template에 담기기는 했는데, `\n`과 같은 문자들도 함께 담기고 해서, 문제가 있는 것 같습니다. 이 부분을 해결해주면 잘 들어갈 것 같은데 말이죠. 

```python
@app.route('/plot_template')
def plot_template():
    from bokeh.plotting import figure
    from bokeh.embed import components

    plot = figure()
    plot.circle([1,2], [3,4])

    script, div = components(plot)
    #script = json.dumps(script, ensure_ascii=False, indent='\t')
    #div = json.dumps(div, ensure_ascii=False, indent='\t')
    return render_template('plot_template.html', plot1_script=script, plot1_div=div)
```