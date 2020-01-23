---
title: 3개월동안 먹은 커피 기록을 분석합니다. 
category: data-analysis
tags: python python-lib data-science quantify-myself numpy matplotlib seaborn pandas time-series
---

## 3개월동안 마신 커피 데이터를 분석합니다. 

- 3월 초부터 6월 19일까지 저는 잠시 대학원을 떠나 집에서 머물고 있었습니다. 저는 집에서는 공부를 못해서 늘 집앞에서 커피를 먹으면서 공부를 했습니다. 문득 카드 사용 내역을 보는데, 이걸 활용해서 뭔가 재밌는 것을 할 수 있지 않을까? 생각했어요. 그래서 간단하게 분석을 해봤습니다. 
- 미리 말씀드리지만, 매우 간단해요. 
- 다만, dataframe의 index를 time series로 관리할 경우, 편한 부분들이 이 케이스를 통해서 드러난다고 할 수 있겠네요. 
    - 예를 들어서, `resample`를 쓰면 `groupby`와 유사하게 기간별로 aggregate할 수 있다는 것

## do it. 

- 데이터는 구글 시트에 저장했습니다. 그런데, 구글 시트에서 바로 긁어오는 부분이 쉽지 않아서, 그냥 컨씨 컨브이하여 텍스트로 만들고 텍스트로부터 읽어왔습니다. raw data는 제일 아래에 저장해두었습니다. 

### data reading and preprocessing 

- 간단하게, 텍스트 데이터를 읽은 다음, date와 time을 datetime format으로 변환해줍니다. `pandas.DataFrame`의 index가 datetime으로 되어 있어야 이후 처리가 편해집니다. 

```python
import pandas as pd
import datetime as dt 
import matplotlib.pyplot as plt
import seaborn as sns

weeknum_to_dict = {0:'mon', 1:'tue', 2:'wed', 3:'thu', 4:'fri', 5:'sat', 6:'sun'}

df = pd.DataFrame(list(map(lambda s: s.split("\t"), input_text.split("\n"))), 
                  columns = ['date', 'time', 'cost']
                 )
# date preprocessing
df['date_time'] = df['date']+df['time']
df['date_time'] = df['date_time'].apply(lambda x: dt.datetime.strptime(x, '%Y. %m. %d.%H:%M'))
df = df[['date_time', 'cost']]
df['cost'] = df['cost'].astype('float64')
df = df.set_index('date_time')
"""
- 비어 있는 날짜도 모두 추가해서 Index에 집어넣습니다. 
"""
date_index = pd.date_range(df.index.min().date(), df.index.max().date())
df_all_date = pd.Series([0 for i in range(0, len(date_index))], index=date_index)
timestamp = pd.Series([[] for i in range(0, len(date_index))], index=date_index)
for row in df.iterrows():
    df_all_date[row[0].date()]+=row[1]['cost']
    timestamp[row[0].date()].append(row[0])
df_all_date = pd.DataFrame(df_all_date, columns=['cost'])

df_all_date['weekday'] = [d.weekday() for d in df_all_date.index]
df_all_date['timestamp'] = timestamp
# study_time의 경우는, 찍혀 있는 timestamp의 max에서 min을 빼줍니다. 그다음 3600으로 나누어주면 시간이 됩니다. 
df_all_date['study_time'] = df_all_date['timestamp'].apply(
    lambda ts: 0 if len(ts)==0 else (max(ts)-min(ts)+dt.timedelta(2/24, 0, 0)).seconds/3600
)
df_all_date = df_all_date[2:]# 3월부터 고려함
print(df_all_date.head(5))
```

```
            cost  weekday                                   timestamp  \
2018-03-01     0        3                                          []   
2018-03-02  6000        4  [2018-03-02 18:11:00, 2018-03-02 15:13:00]   
2018-03-03     0        5                                          []   
2018-03-04  6000        6  [2018-03-04 17:09:00, 2018-03-04 15:02:00]   
2018-03-05  6000        0  [2018-03-05 16:54:00, 2018-03-05 12:53:00]   

            study_time  
2018-03-01    0.000000  
2018-03-02    4.966667  
2018-03-03    0.000000  
2018-03-04    4.116667  
2018-03-05    6.016667  
```

### font customizing 

- 아래 코드를 사용하면, 해당 jupyter notebook에서 사용하는 모든 font의 기본 성질이 변경됩니다. 

```python
font_path = '/Users/frhyme/Library/Fonts/BMJUA_otf.otf'
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rcParams['font.family'] = font_name
plt.rcParams['font.size'] = 15
```

- 아래에서 선언한, 각각 변수를 `matplotllib`의 개별 요소에 fontproperties에 넣어서 사용할 수 있습니다. 

```python
import matplotlib.font_manager as fm

BMDOHYEON = fm.FontProperties(fname='/Users/frhyme/Library/Fonts/BMDOHYEON_otf.otf')
BMJUA = fm.FontProperties(fname='/Users/frhyme/Library/Fonts/BMJUA_otf.otf')
BMHANNA = fm.FontProperties(fname='/Users/frhyme/Library/Fonts/BMHANNA_11yrs_otf.otf')
SDMiSaeng = fm.FontProperties(fname='/Users/frhyme/Library/Fonts/SDMiSaeng.ttf')
nanum = fm.FontProperties(fname='/Library/Fonts/NanumSquareOTFB.otf')
TimesNewRoman = fm.FontProperties(fname='/Library/Fonts/Times New Roman.ttf')
```

### plotting 

- 그림을 그립니다. 간단하게 `resample`와 `groupby`를 이용하여, 새로운 테이블을 만들어서 그대로 plotting해주거나, 
- `heatmap`의 경우에는 `pivot`을 사용하여 새로운 테이블을 만들어서, 넘겨줍니다. 

```python
## 1) 주별 사용 금액 변화 
plt.figure(figsize=(12, 4))
week_grp = df_all_date.resample("W")['cost'].sum()
week_grp.plot(marker='o', markersize=15, color='red', 
              linestyle='--', linewidth=2)
plt.gca().set_xlim(min(week_grp.index)-1, max(week_grp.index)+1)
plt.gca().set_ylim(0, 65000)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
#plt.gca().spines['left'].set_visible(False)
#plt.gca().spines['bottom'].set_visible(False)
plt.title('1) 주별 사용금액 변화', color='black', fontsize=20)
plt.savefig('../../assets/images/markdown_img/180619_0531_week_grp_cost.svg')
plt.show()

## 2) 요일별 사용 금액 변화 
plt.figure(figsize=(12, 4))
weekday_grp = df_all_date.groupby('weekday')['cost'].sum()
weekday_grp.plot(marker='o', markersize=20, color='green', 
                 linestyle='--', linewidth=3)
plt.title('2) 요일별 사용금액 변화', color='black', fontsize=20)
plt.gca().set_xlim(-0.5, 6.5)
plt.gca().set_xticklabels(['', 'MON', 'TUE', 'WED', 'THU', "FRI", 'SAT', 'SUN'])
plt.gca().set_ylim(35000, 100000)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.savefig('../../assets/images/markdown_img/180619_0531_weekday_grp_cost.svg')
plt.show()

## 3) heatmap(index=weeks, columns=weekday)
weeknum_to_dict = {0:'mon', 1:'tue', 2:'wed', 3:'thu', 4:'fri', 5:'sat', 6:'sun'}
df_cost_grp_week = df_all_date.reset_index().pivot('index', 'weekday', 'cost').fillna(0).resample('w').sum()
df_cost_grp_week.index = ["{}, {}w".format(ind.strftime("%b"), ind.day//7 + 1) for ind in df_cost_grp_week.index]
df_cost_grp_week.columns = [weeknum_to_dict[col].upper() for col in df_cost_grp_week.columns]

plt.figure(figsize=(10, 10))
sns.heatmap(df_cost_grp_week, 
            cmap=plt.cm.Spectral, 
            linewidths=(5), cbar=False, annot=True, fmt=".0f",
            mask = df_cost_grp_week.applymap(lambda x: True if x==0 else False)
)
plt.gca().xaxis.tick_top() 
plt.xticks(fontproperties=BMDOHYEON, fontsize=15, )
plt.yticks(fontproperties=BMDOHYEON, fontsize=15, )
plt.xlabel('')
# 지금 xticklabels를 위로 올렸기 때문에, plt.title대신 plt.text를 사용. 
plt.text(1.5, -1.5, '3) 주별/요일별 사용금액 heatmap', fontsize=25, color='darkblue')
plt.savefig('../../assets/images/markdown_img/180619_0531_week_grp_cost_heatmap.svg')
plt.show()
```

- 그림을 보면, 첫주에는 열심히 하다가, 점점 게을러지고, 끝즈음에는 다시 열심히 하구요. 

![](/assets/images/markdown_img/180619_0531_week_grp_cost.svg)

- 토요일에는 데이트를 하기 때문에, 공부를 게을리하고요... 

![](/assets/images/markdown_img/180619_0531_weekday_grp_cost.svg)

- heatmap에서도 처음에는 열심히 하다가 나중에는 매우 게으른 것을 볼 수 있습니다. 

![](/assets/images/markdown_img/180619_0531_week_grp_cost_heatmap.svg)

## wrap-up

- 쓰고나니 또 아주 간단하군요 하하하하 
