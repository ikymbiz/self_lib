"""tips()
> .pd      pd.DataFrame / pd.Series
> .pd_iloc 位置指定取得
> .pd_iloc 位置指定取得

> .r       Read data

> .kata    型
> .date    日付型
>
>
>
>
"""
    
def pd():
    """
> DataFrame:
https://pandas.pydata.org/pandas-docs/stable/reference/frame.html\n
import pandas as pd
data = pd.DataFrame({"ID"  : ["",""],
                     "colA": ["",""],
                     "colB": ["",""],
                     "colC": ["",""]})

> Series:
data = pd.Series(["","","",""],name="col")
data = pd.Series(list,name="col")
    """
        
def pd_iloc():
    """
- 位置指定取得
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html

# dataの四行目(0から数えて4番目)のscore1の値
data.iat[4,1]

# dataの2-3行目
data.iloc[2:4]

# dataの2-3行目の2列目
data.iloc[2:4,1]

# dataの2-3行目
data[2:4]
    """

def r():
    """
read data:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html

[csv]
import pandas as pd
data=pd.read_csv('tips.csv',index=False)
data=pd.read_csv('tips.csv',index_col(0))

[Excel]
$ pip install xlrd-1.2.0
import xlrd
data=pd.read_excel('tips.xlsx')

[pickle]
import pickle
data=pd.read_pickle("tips.pkl")
    """
    
def kata():
    """
> 型:
https://punhundon-lifeshift.com/python_list_numpy_series_dataframe_convert

> 型の確認:
- type(data)
- data.dtypes
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html

> 型の変更:
data['colA']=data['colA'].astype('float')
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.astype.html

> リスト -> Numpy配列:
ndarray = np.array(list)

> リスト -> Series
pd.Series = pd.Series(list)
pd.Series = pd.Series(list, index = ['colA','colB','colC','colD'])

> Numpy配列 -> リスト
list = data.tolist(ndarray)

> Numpy配列 -> Series
pd.Series = pd.Series(ndarray)
pd.Series = pd.Series(ndarray, index = ['colA','colB','colC','colD'])

> Series -> Numpy配列
ndarray = pd.Series.values

> Series -> リスト
ndarray = pd.Series.values.tolist()

> Series -> DataFrame
df = pd.DataFrame(pd.Series)
df = pd.DataFrame(pd.Series, columns = ['colA'])

> DataFrame -> Series
pd.Series = df['colA']
pd.Series = df.colA



>> see also
to_datetime()
Convert argument to datetime.

to_timedelta
Convert argument to timedelta.

to_numeric
Convert argument to a numeric type.

    """

def date():
    """日付型
date=pd.to_datetime(str_date)

    """