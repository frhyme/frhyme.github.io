---
title: flask와 pandas를 연결해봅시다. 
category: python-lib
tags: flask pandas python python-lib html excel dataframe css 
---

## flask와 pd.DataFrame 연동하기 

- 저는 데이터는 일단 엑셀 파일로 들어온다고 가정합니다. 따라서 `pandas`를 이용해서 엑셀을 dataframe로 변환해서 처리하는 것이 반드시 필요하죠. 
- flask에서 dataframe를 연동하는 것에 문제가 없는지 확인해봅니다. 

## make and read excel file 

- 아래 코드를 이용해서 url 요청이 오면 엑셀 파일을 만들고 엑셀 파일을 html로 변환해주는 형식으로 처리했습니다. 
- `python run.py`를 수행하면 알아서 엑셀 파일이 만들어지고 해당 엑셀 파일을 읽고 html로 변환하여 화면에 뿌려줍니다. 
- 아래 코드만으로 수행하면, 어쨌든 웹 브라우저에서 dataframe의 내용이 그대로 뜹니다. 일단 이정도로만 해도 뭐 일단 보기는 문제가 없죠. 

- `css`를 이용해서 더 예쁘게 만들 수 있을 것 같기는 하네요. 

```python
from flask import Flask

app = Flask(__name__, static_url_path='/static')

@app.route('/pandas')
def make_read_excel():
    ## 반드시 static에 있지 않아도 읽을 수는 있음.
    ## 현재 파일과 읽으려는 파일이 같은 경로에 있기 때문에 아래와 같은 방식으로 읽을 수도 있음.
    import pandas as pd 
    import numpy as np 

    ## make excel file 
    writer = pd.ExcelWriter('static/excel_for_flask.xlsx')
    df = pd.DataFrame({"col_{}".format(i):list(np.random.randint(0, 100, 100)) for i in range(0, 8)})
    df.to_excel(writer, 'sheet1')
    writer.save()

    ## read excel file 
    df = pd.read_excel('static/excel_for_flask.xlsx')
    ## 아주 다행히도, dataframe을 html 문서로 바로 변환해주는 형식이 있습니다. 
    return df.to_html()

if __name__ == '__main__':
    # threaded=True 로 넘기면 multiple plot이 가능해짐
  app.run(debug=True, threaded=True)
```

- 다음처럼 표시됩니다. 
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col_0</th>
      <th>col_1</th>
      <th>col_2</th>
      <th>col_3</th>
      <th>col_4</th>
      <th>col_5</th>
      <th>col_6</th>
      <th>col_7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>7</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>9</td>
      <td>1</td>
      <td>9</td>
      <td>7</td>
      <td>1</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8</td>
      <td>7</td>
      <td>6</td>
      <td>4</td>
      <td>9</td>
      <td>7</td>
      <td>9</td>
      <td>5</td>
    </tr>
  </tbody>
</table>

## styling

- dataframe을 html로 변환하는 과정에서 뭐 적당히 나쁘지 않게 나오기는 했는데, 썩 마음에 들지는 않습니다. 
    - `df.to_html()`로 값만 받은 다음에 css를 embed하여 처리하는 것이 더 낫지 않을까 싶기는 합니다만. 
- `pandas`에서 직접 스타일링을 하여 넘겨줄 수도 있습니다. 
- 테이블 간의 간격이나, 문제가 되는 포인트를 색깔로 구분할 수 있게 보여주면 훨씬 좋을 것 같아요. 

```python
@app.route('/pandas')
def make_read_excel():
    ## 반드시 static에 있지 않아도 읽을 수는 있음.
    ## 현재 파일과 읽으려는 파일이 같은 경로에 있기 때문에 아래와 같은 방식으로 읽을 수도 있음.
    import pandas as pd 
    import numpy as np 

    ## make excel file 
    writer = pd.ExcelWriter('static/excel_for_flask.xlsx')
    df = pd.DataFrame({"col_{}".format(i):list(np.random.randint(0, 10, 10)) for i in range(0, 8)})
    df.to_excel(writer, 'sheet1')
    writer.save()

    ## read excel file 
    df = pd.read_excel('static/excel_for_flask.xlsx')
    
    ## styling을 해봅시다. 
    ## cell의 값을 기준으로 스타일링하기 
    ## 아래 함수를 사용하여 style.applymap(color_extreme) 로 넘겨주면 적용됨 
    def color_extreme(val):
        if val==0:
            return 'color: {}'.format('red')
        elif val==9:
            return 'color: {}'.format('blue')
        else:
            return 'color: {}'.format('black')
    df_with_style = df.style.applymap(color_extreme)

    ## data의 format을 변경할 때 
    df_with_style = df_with_style.format("{:.2f}")
    ## 전체 프로퍼티를 변화하고 싶을 때 
    df_with_style.set_properties(**{
        'background-color':'white', 
        'border':'1px solid black',
        'font-size': '20px', 
    })
    ## 요소 별로 변화시키고 싶을 때
    styles = [
        {'selector':'td', 
         'props':[('text-align', 'center'), ('font-size', '20px'), ('height', '50px'), ('width', '100px')
         ]}, 
        {'selector':'tr', 'props':[('font-size', '30px')]}
    ]
    df_with_style = df_with_style.set_table_styles(styles)

    ## matplotlib의 colormap을 이용하여 cell의 값 정도를 표시하고 싶을 때 
    df_with_style = df_with_style.background_gradient(cmap='Reds')
    
    #df_with_style = df_with_style.set_table_styles(styles)
    ## html로 렌더링해주어야 함 
    return df_with_style.render()
```

- 결과는 다음처럼 표시됩니다. 

<style  type="text/css" >
    #T_f563bff6_8a62_11e8_9819_9a000138b130 td {
          text-align: center;
          font-size: 20px;
          height: 50px;
          width: 100px;
    }    #T_f563bff6_8a62_11e8_9819_9a000138b130 tr {
          font-size: 30px;
    }    #T_f563bff6_8a62_11e8_9819_9a000138b130row0_col0 {
            color:  black;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #fcc4ad;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row0_col1 {
            color:  black;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #aa1016;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row0_col2 {
            color:  black;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #fff5f0;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row0_col3 {
            color:  black;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #fcbba1;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row0_col4 {
            color:  black;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #fff5f0;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row0_col5 {
            color:  black;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #fc9272;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row0_col6 {
            color:  black;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #fff5f0;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row0_col7 {
            color:  black;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #67000d;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row1_col0 {
            color:  red;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #fff5f0;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row1_col1 {
            color:  blue;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #67000d;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row1_col2 {
            color:  black;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #fb694a;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row1_col3 {
            color:  black;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #67000d;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row1_col4 {
            color:  black;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #67000d;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row1_col5 {
            color:  black;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #67000d;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row1_col6 {
            color:  black;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #67000d;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row1_col7 {
            color:  black;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #67000d;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row2_col0 {
            color:  blue;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #67000d;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row2_col1 {
            color:  black;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #fff5f0;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row2_col2 {
            color:  black;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #67000d;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row2_col3 {
            color:  black;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #fff5f0;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row2_col4 {
            color:  black;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #67000d;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row2_col5 {
            color:  red;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #fff5f0;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row2_col6 {
            color:  black;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #fdd4c2;
        }    #T_f563bff6_8a62_11e8_9819_9a000138b130row2_col7 {
            color:  black;
            background-color:  white;
            border:  1px solid black;
            font-size:  20px;
            background-color:  #fff5f0;
        }</style>  
<table id="T_f563bff6_8a62_11e8_9819_9a000138b130" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >col_0</th> 
        <th class="col_heading level0 col1" >col_1</th> 
        <th class="col_heading level0 col2" >col_2</th> 
        <th class="col_heading level0 col3" >col_3</th> 
        <th class="col_heading level0 col4" >col_4</th> 
        <th class="col_heading level0 col5" >col_5</th> 
        <th class="col_heading level0 col6" >col_6</th> 
        <th class="col_heading level0 col7" >col_7</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_f563bff6_8a62_11e8_9819_9a000138b130level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row0_col0" class="data row0 col0" >2.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row0_col1" class="data row0 col1" >8.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row0_col2" class="data row0 col2" >1.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row0_col3" class="data row0 col3" >3.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row0_col4" class="data row0 col4" >3.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row0_col5" class="data row0 col5" >3.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row0_col6" class="data row0 col6" >1.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row0_col7" class="data row0 col7" >5.00</td> 
    </tr>    <tr> 
        <th id="T_f563bff6_8a62_11e8_9819_9a000138b130level0_row1" class="row_heading level0 row1" >1</th> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row1_col0" class="data row1 col0" >0.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row1_col1" class="data row1 col1" >9.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row1_col2" class="data row1 col2" >2.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row1_col3" class="data row1 col3" >6.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row1_col4" class="data row1 col4" >5.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row1_col5" class="data row1 col5" >8.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row1_col6" class="data row1 col6" >7.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row1_col7" class="data row1 col7" >5.00</td> 
    </tr>    <tr> 
        <th id="T_f563bff6_8a62_11e8_9819_9a000138b130level0_row2" class="row_heading level0 row2" >2</th> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row2_col0" class="data row2 col0" >9.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row2_col1" class="data row2 col1" >2.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row2_col2" class="data row2 col2" >3.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row2_col3" class="data row2 col3" >2.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row2_col4" class="data row2 col4" >5.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row2_col5" class="data row2 col5" >0.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row2_col6" class="data row2 col6" >2.00</td> 
        <td id="T_f563bff6_8a62_11e8_9819_9a000138b130row2_col7" class="data row2 col7" >2.00</td> 
    </tr></tbody> 
</table> 


## wrap-up

- 그냥 css로 적용하는 것이 좋을 수도 있겠지만, 값에 따라서 엑셀처럼 다른 형식으로 보여주는 것들은 좋은 것 같아요. 

## reference 

- <https://pandas.pydata.org/pandas-docs/stable/style.html>

## raw code

```python
from flask import Flask

app = Flask(__name__, static_url_path='/static')

@app.route('/pandas')
def make_read_excel():
    ## 반드시 static에 있지 않아도 읽을 수는 있음.
    ## 현재 파일과 읽으려는 파일이 같은 경로에 있기 때문에 아래와 같은 방식으로 읽을 수도 있음.
    import pandas as pd 
    import numpy as np 

    ## make excel file 
    writer = pd.ExcelWriter('static/excel_for_flask.xlsx')
    df = pd.DataFrame({"col_{}".format(i):list(np.random.randint(0, 10, 3)) for i in range(0, 8)})
    df.to_excel(writer, 'sheet1')
    writer.save()

    ## read excel file 
    df = pd.read_excel('static/excel_for_flask.xlsx')
    return df.to_html()
    
    ## styling을 해봅시다. 
    ## cell의 값을 기준으로 스타일링하기 
    ## 아래 함수를 사용하여 style.applymap(color_extreme) 로 넘겨주면 적용됨 
    def color_extreme(val):
        if val==0:
            return 'color: {}'.format('red')
        elif val==9:
            return 'color: {}'.format('blue')
        else:
            return 'color: {}'.format('black')
    df_with_style = df.style.applymap(color_extreme)

    ## data의 format을 변경할 때 
    df_with_style = df_with_style.format("{:.2f}")
    ## 전체 프로퍼티를 변화하고 싶을 때 
    df_with_style.set_properties(**{
        'background-color':'white', 
        'border':'1px solid black',
        'font-size': '20px', 
    })
    ## 요소 별로 변화시키고 싶을 때
    styles = [
        {'selector':'td', 
         'props':[('text-align', 'center'), ('font-size', '20px'), ('height', '50px'), ('width', '100px')
         ]}, 
        {'selector':'tr', 'props':[('font-size', '30px')]}
    ]
    df_with_style = df_with_style.set_table_styles(styles)

    ## matplotlib의 colormap을 이용하여 cell의 값 정도를 표시하고 싶을 때 
    df_with_style = df_with_style.background_gradient(cmap='Reds')
    
    #df_with_style = df_with_style.set_table_styles(styles)
    ## html로 렌더링해주어야 함 
    return df_with_style.render()

if __name__ == '__main__':
    # threaded=True 로 넘기면 multiple plot이 가능해짐
  app.run(debug=True, threaded=True)
```