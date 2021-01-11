"""tips()
> .pd      pd.DataFrame / pd.Series
> .pd_iloc 位置指定取得
> .pd_iloc 位置指定取得

> .r       Read data
> .pd_iloc
> .kata    型
> .date    日付型
> .pickle
> .json
> .txt
> .urllib
> .sequence
> .list_in_list
> .getattr_
> .generater
> .err
> .exception
> .itertool
> .os
> .performance
> .
> .
> .
> .
> .
> .
> .
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

> 日時
import datetime
now = datetime.datetime.now()
now.year
now.month
now.day
now.hour
now.minute
now.second
now.microsecond

# 日時の格納
dt = datetime.datetime(2020,12,10,16,18)

# 時間差
delta = now - dt

# 時間の合計 → .total_seconds()
delta.total_seconds()

# 曜日の取得 → .weekday()
dt.weekday()
0:Mon / 1:Tue / 2:Wed / 3:Thu / 4:Fri / 5:Sat / 6:Sun

# 日付型から文字列へ変換する
now = datetime.datetime.now()
now.strftime('%Y/%m/%d')
now.strftime('%Y/%m/%d %H:%M:%S')

# 文字列から日付型へ変換する
datetime.datetime.strptime('2020/01/01', '%Y/%m/%d')

# datetimeの日付の計算（足し算、引き算）
import datetime

#datetimeの日付の計算
#     weeks, days, hours, minutes, seconds

now = datetime.datetime.now() # => datetime.datetime(2019, 8, 2, 1, 59, 33, 338054)

# 1週 加算
now + datetime.timedelta(weeks=1) # => datetime.datetime(2019, 8, 9, 1, 59, 33, 338054)
# 10日 減算
now - datetime.timedelta(days=10) # => datetime.datetime(2019, 7, 23, 1, 59, 33, 338054)
# 10時間 加算
now + datetime.timedelta(hours=10) # => datetime.datetime(2019, 8, 2, 11, 59, 33, 338054)
# 10分 減算
now - datetime.timedelta(minutes=10) # => datetime.datetime(2019, 8, 2, 1, 49, 33, 338054)
# 10秒 加算
now + datetime.timedelta(seconds=10) # => datetime.datetime(2019, 8, 2, 1, 59, 43, 338054)

# 7日, 1時間, 10分 加算
now + datetime.timedelta(days=7, hours=1, seconds=10) # => datetime.datetime(2019, 8, 9, 2, 59, 43, 338054)

https://qiita.com/7110/items/4ece0ce9be0ce910ee90

# 月末を求める
import calendar

month_range = calendar.monthrange(2018, 5)

print(month_range) # (1, 31)

# 要素を指定すれば末日だけ取得できます
print(month_range[1]) #31

# うるう年でもちゃんと末日を取得してくれます
month_range = calendar.monthrange(2020, 2)[1]

print(month_range) # 29

'''''''''''''''
import calendar
import datetime

y = 2020
m = 2

date = datetime.date(y, m, calendar.monthrange(y, m)[1])
print(date) # 2020-02-29
'''''''''''''''

# Nヶ月後を求める
$ pip install python-dateutil

from dateutil.relativedelta import relativedelta

date = datetime.date(2018, 5, 1)
print(date) # 2018-05-01

# 1ヶ月後を求める
print(date + relativedelta(months=1)) # 2018-06-01

# 1ヶ月前を求める
print(date + relativedelta(months=-1)) # 2018-04-01

# 1日後を求める
print(date + relativedelta(days=1)) # 2018-05-02

# 1日前を求める
print(date + relativedelta(days=-1)) # 2018-04-30

# 1年後を求める
print(date + relativedelta(years=1)) # 2019-05-01

# 1年前を求める
print(date + relativedelta(years=-1)) # 2017-05-01

https://codelab.website/python-datetime-control/

# 日付型の差
import datetime

def f11_2(dt1, dt2):

    Parameters
    ----------
    dt1 : datetime.datetime
    dt1 : datetime.datetime
    
    Returns
    -------
    str
        "{days}日{hour}時間{minutes}分{seconds}秒"

    dt = dt2 - dt1
    dt_date = dt.days
    dt_seconds = dt.seconds
    dt_min, dt_sec = divmod(dt_seconds, 60)
    dt_hour, dt_min = divmod(dt_min, 60)
    return f'{dt_date}日{dt_hour}時間{dt_min}分{dt_sec}秒'

https://www.tech-teacher.jp/blog/python-datetime/
https://note.nkmk.me/python-datetime-timedelta-conversion/
    """

def pickle():
    """pickle

  オブジェクトの永続性を実現する

PythonObject   ⇔ 　バイトオブジェクト　⇔　ディスク
	　　 直列化		      永続化

# pickleで保存する
import pickle
with open('li_pickle','wb') as f:
    pickle.dump(li,f)

# pickleで読込む
import pickle
with open('li.pickle','rb') as f:
    li = pickle.load(f)
    """
    
def json():
    """
    > json
  JavaScript Object Notationの略



# JSONをPythonのデータ型に変換する
> json.loads(JSON文字列)

import json
from collections import OrderedDict
import pprint

s = r'{"C": "\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}'

print(s)
# {"C": "\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}

d = json.loads(s)

pprint.pprint(d, width=40)
# {'A': {'i': 1, 'j': 2},
#  'B': [{'X': 1, 'Y': 10},
#        {'X': 2, 'Y': 20}],
#  'C': 'あ'}

print(type(d))

> json.load(ファイル)

with open('data/src/test.json') as f:
    df = json.load(f)

pprint.pprint(df, width=40)
# {'A': {'i': 1, 'j': 2},
#  'B': [{'X': 1, 'Y': 10},
#        {'X': 2, 'Y': 20}],
#  'C': 'あ'}

print(type(df))


  JSONの型		Pythonの型
  object		dictionary
  array			list
  string		string
  number(int)		int
  number(real)		float
  true			True
  false			False
  null			None

> example

from urllib.request import urlopen
from json import loads

url = 'https://api.github.com/users/gvanrossum/repos'
body = request.urlopen(url).read()
body = body.decode('utf-8')
repos = loads(body)
for r in repos:
    print(r['name'])


# Pythonのデータ型をJSONに変換する
> json.dumps(Pythonのオブジェクト[,オプションの引数...])

> JSONファイルの新規作成

d_new = {'A': 100, 'B': 'abc', 'C': 'あいうえお'}

with open('data/dst/test_new.json', 'w', encoding="utf8") as f:
    json.dump(d_new, f, indent=2, ensure_ascii=False)

> JSONファイルの更新（修正・追記）
# open()でパスを指定しjson.load()で既存のJSONファイルを読み込み。
# 元の並びを保持したい場合は、引数object_pairs_hook=OrderedDictとする。

with open('data/dst/test_new.json') as f:
    d_update = json.load(f, object_pairs_hook=OrderedDict)

print(d_update)

# 辞書オブジェクトを適宜更新。
d_update['A'] = 200
d_update.pop('B')
d_update['D'] = 'new value'

print(d_update)

# open()でパスを指定しjson.dump()で適宜整形して保存。
# 便宜上、例では新しいパスを指定しているが、
# 元のファイルパスを指定すると上書きとなる。

with open('data/dst/test_new_update.json', 'w') as f:
    json.dump(d_update, f, indent=2, ensure_ascii=False)

# 結果を確認。
with open('data/dst/test_new_update.json') as f:
    print(f.read())


> json.dump(Pythonのオブジェクト,ファイル)
    """
    
def txt():
    """
    #> txt
import os

# 絶対パスを取得
filePath = os.path.abspath("test.txt")
print(filePath)

# file読込み
with open(filePath,"r",encoding="utf-8") as file:
    data=file.read()
print(data)

# 1行ずつ読込む
i=0
file = open(filePath,"r",encoding='utf-8') 
for line in file:
    i+=1
    print(i,line)

# ファイルを作成し書き込む
file = open ('t.txt','w',encoding='utf-8')
file.write('null')

# ファイルの存在確認をして追記する
str='\ntest'
if os.path.isfile(filePath):
    file = open(filePath,"a+",encoding='utf-8') 
    file.write(str)

# 行を指定して書き込む
with open(filePath,"r",encoding='utf-8') as file:
    lst=file.readlines()
lst.insert(1,'second line\n')

with open(filePath,"w",encoding='utf-8') as file:
    file.writelines(lst)

# ファイルの削除
os.remove('t.txt')
    """

def urllib():
    """
    > urllib
インターネット上のデータを取得する

# urlを指定してファイルを取得する
> urllib.request.urlretrieve(url [,ファイル [, POST用のデータ]])
保存用のファイル名はオプションだが、省略すると一時ファイル用のディレクトリに
保存しようとする。->実務上はファイル名を指定して利用すること。

from urllib import request
from urllib import parse
url = 'h~~~t~~~t^^^p
//dname.com/somefile.zip'
filename = parse.urlparse(url)[2].split('/')[-1]

filename
request.urlretrieve(url,filename)

# URLから取得したデータをオブジェクトで返す
> request.urlopen(url[, POST用のデータ[, タイムアウト]])

メソッド
Fはurlopen()が返すファイル風オブジェクト
	# 連続してデータを読み込む
	>> F.read([整数のサイズ])

	# データから1行読み込む
	>> F.readline([整数のサイズ])

	# 行単位で連続的に読み込む
	>> readlines([整数のサイズ])

	# URLを返す
	>> F.geturl()

	# メタ情報を返す
	>> F.info()
    """

def sequence():
    """
    > シーケンス型
複数の要素が順番に並んだデータのこと
>> 文字列型、タプル型、リスト型

> シーケンス型の演算

演算		結果
x in s		sのある要素が x と等しければ True 、そうでなければ False を返す
x not in s	sのある要素が x と等しければ False 、そうでなければ True を返す
s + t		sと t の結合したものを返す
s * n		s自身を n 回結合したものを返す
s[i] 		0から数えて i 番目の要素を返す
s[i:j:k] 	iから j 番目までステップ k のスライス返す
len(s)		sの長さを返す
min(s)		sの最小の要素を返す
max(s)		sの最大の要素を返す
s.count(x)	s中にxが出現する回数を返す


メソッド/説明/対応するデータ型/返値
> startswith
  文字列が引数の検索したい文字列で始まっているかを確認する
  文字列型
  True/False

> endswith
  文字列が引数の検索したい文字列で終わっているかを確認する
  文字列型
  True/False

> find()
  要素の存在を確認する
  文字列型
  数値型(インデックス値

> index()
  要素の存在を確認する
  文字列型/タプル型/リスト型
  数値型(インデックス値

> replace()
  部分文字列を新しい文字列に置き換える
  文字列型
  文字列型

> strip()
  文字列の先頭および末尾部分を取り除く
  文字列型
  文字列型

> split()
  文字列を区切り文字列で分割する
  文字列型
  リスト型
> join()
  文字列の連結を行うことができる
  文字列型
  文字列型

> sort()
  リスト型のオブジェクト自体の要素を並べ替える
  リスト型
  リスト型
	> li.sort([key=並べ替えの基準,reverse=True/False])
	> li.sort(key=lambda x:x[2]) 文字列の２文字目を基準に並べ替える

> sorted()
  要素を並べ替えて新しいリスト型のオブジェクトを生成する
  文字列型/タプル型/リスト型/セット型/ディクショナリ型
  リスト型

> all()
  すべての要素が真であるかどうかを判定する
  文字列型/タプル型/リスト型/セット型/ディクショナリ型
  True/False

> any()
  一部の要素が真であるかどうかを判定する
  文字列型/タプル型/リスト型/セット型/ディクショナリ型
  True/False

>get()
  キーが引数と同じかを確認する
  ディクショナリ型
  ディクショナリ型

> update()
  セット型のオブジェクト自体に要素を追加
  セット型
  セット型

  二つのディクショナリを組み合わせる
  ディクショナリ型
  ディクショナリ型
    """
def list_in_list():
    """
    > 内包表記

変数　= 要素について行う処理 for 任意の変数 in 複数の要素を持つオブジェクト

同じ処理を内包表記を使わずに書くと、、、

リスト/セット/ディクショナリの初期値の変数
for 任意の変数 in 複数の要素を持つオブジェクト:
    要素について行う処理

> example1
  even_list = [i for i in range(10) if i % 2 == 0]

  even_list = []
  for i in range(10):
      if i % 2 == 0:
         even_list.append(i)

> example2
  even_list = [i if i % 2 == 0 else "odd" for i in range(10)]

  even_list = []
  for i in range(10):
      if i % 2 == 0:
         even_list.append(i)
      else:
         even_list.append("odd")

> example3	三項演算子
  "even" if True else "odd"


##　まとめ
else の有無			位置		構文					要素数
if ... のみを使うとき		ifは後ろ	[ ... for ... in ... if ... ]		ifの条件に合致しないと要素が減る
if ... else ... を使うとき	ifは前		[ ... if ... else ... for ... in ... ]	要素数は減らない
    """
    
def getattr_():
    """
    > getattr()
Pythonの組み込み関数の一つで、オブジェクトで指定された属性の値を返す関数
属性とは、クラスのメンバー変数のこと
オブジェクトの属性の値の他にオブジェクト内で定義された値を取り出すことができる

> getattr(object, name[, default])()

> exaample
class Spam:
    def ham(self):
        return "ham"

    def egg(self):
        return "egg"

    def bacon(self):
        return "bacon"

    def tomatoes(self):
        return "tomatoes"


spam = Spam()


def execute_spam(text):
''''''
    Parameters
    ----------
    text : str
        実行する関数の文字列
    
    Returns
    -------
    spam.{関数名}の実行結果
''''''
    cl = Spam() 
    
    return getattr(cl, text)()


# assert execute_spam("ham") == "ham"
    """

def generater():
    """
    > ジェネレータ（内部イテレータ）
  イテレータを簡単に定義するための仕組み
  return のかわりに yeld文を使って戻り値を返す関数を定義する

# ジェネレータ関数
> example
def get_primes(x=2):
    while True:
        for i in range(2,x):
	    if x%i ==0:
		break
	else:
	    yield x
	
	x += 1

i = get_primes()
for c in range(10):
    print(next(i))

> yeld とは「譲る」という意味
> 上記のようにｘが無限のリストを無限リストという

# ジェネレータ式

( 式 for 繰り返し変数 in シーケンス (if 条件式))

> example

i = (x**2 for x in range(1,10))
print(next(i))
print(next(i))
print(next(i))

→前のステップで出力した結果に続けて'式'の処理を続けていく
    """
    
def err():
    """
    > エラー一覧

> SyntaxError
  文法エラー
　->クオーテーション、括弧の付け忘れを確認

> IndentationError
　インデントエラー
　->インデントを確認。
　　	def/classとの関連
　	for/if文の関連
　	例外処理の関連

> Exeption
  プログラムの実行中に起こるエラー

>>NameError
  未定義の変数などを参照しようとしている

>>AttributeError
  -オブジェクトに定義されていないアトリビュートを参照している
  -未定義のメソッドを呼び出そうとしている
　-組込型オブジェクトのように、アトリビュートの追加が許されていない
　 オブジェクトにアトリビュートを代入しようとして失敗している

>>TypeError
  処理の過程でふさわしくない方のオブジェクトが使われている
　-文字列と数値を足している
  -リストの要素を整数以外のインデックスで参照しようとしている
  -組込型のメソッド、関数の引数として想定外の型のオブジェクトが渡されている

>>IndexError
  リストのようなシーケンスをインデックスで参照するとき、要素数を超える数を指定した

>>KeyError
  -ディクショナリの要素をキーで参照するとき、存在しないキーを指定している
　-set型で存在しない要素にアクセスしようとしている

>>ImportError
  import文でモジュール定義を見つけられなかった

>>UnicodeDecodeError/UnicodeEncodeError
  文字列等のデコードエンコードでエラー

>>zeroDivisionError
  数値を0で割ろうとしている

    """
    
def exception():
    """
    > 例外処理
例外が発生すると、tryブロックのそれ以降のプログラムの実行がスキップされる

-> tryで例外が発生したら、except文へジャンプする

> example
import sys

for fn in sys.argv[1:]:
    try:
        f = open(fn)
    except FileNotFoundError:
        print(f'{fn}というファイルは存在しません')
    else:
        try:
              print(fn,len(f.read()))
        finally:
              f.close()

> 例外処理の書式

　except:			　すべての例外を受け取り、例外発生時の処理を行う

  except 例外クラス名:		　クラスを指定して、特定の例外だけを受け取る
				　例外クラスは()で囲み、',コンマ'で区切ることで複数列記可

  except 例外クラス名 as 変数名:　例外クラスと例外オブジェクトを受け取る変数名を指定
				　例外オブジェクトが代入された変数を使って、
				　例外に関するより細かな情報を得ることができる

　else:				  例外が発生しなかった場合の処理を記述

　finally:			  例外が発生してもしなくても、実行するブロック

> 例外を発生させる
　自作クラスなどでエラーが発生したことを外部に伝える

  raise文に例外クラスから作った例外オブジェクトを添えて例外を発生させる
	raise ValueError("Some Message")

> 例外を表示、保存する
import traceback

try:
    # 処理を実行するコード

except:
    traceback.print_exc()
　　# ex = traceback.format_exc()

    """

def itertool():
    """
    > itertools

効率的なループ実行のためのイテレータ生成関数
このモジュールは、高速でメモリ効率に優れ、単独でも組合せても
使用することのできるツールを標準化したものです。
同時に、このツール群は "イテレータの代数" を構成していて、
pure Python で簡潔かつ効率的なツールを作れるようにしています。

> https://docs.python.org/ja/3/library/itertools.html#itertools.product

import itertools
import pprint
li = list(itertools.product('ABCD', 'xy'))
pprint.pprint(li)
    """
    
def os():
    """
    https://note.nkmk.me/python-os-remove-rmdir-removedirs-shutil-rmtree/

import os

os.makedirs('temp/', exist_ok=True)

with open('temp/file.txt', 'w') as f:
    f.write('')

print(os.listdir('temp'))


import os
os.remove('temp/file.txt')
    """

def performance():
    """
    > パフォーマンス分析

## 処理時間の確認方法
  %timeit を使用すると実行時間を計測することができる

> example1
  %timeit オプション 処理時間を確認したい処理コード
→平均実行時間 ± 標準偏差 per loop (mean ± std. dev. of 試行回数 runs, コードの実行回数 loops each)

> example2
  li = list(range(1, 1_000_000))
  %timeit 5_000_000 in li
→12.2ms ±　269 µs per loop (mean ±　std. dev. of 7 runs, 100 loops each)

## メモリ使用量の確認方法
  sys モジュールの getsizeof メソッドを使ってオブジェクトに直接起因するメモリ消費を確認できる
  引数のオブジェクトのサイズをバイト数で返す

 import sys
 sys.getsizeof(メモリ使用量を確認するオブジェクト)

## セットの 処理時間の確認方法
  セットの探索にかかるコストは要素数に依存しない
  リストの探索にかかるコストは要素数に応じて増加する
  頻繁に要素の参照を行うのであればリストではなくセットを使うのがよい

  items_in_set= set(li)
  %timeit 5_000_000 in li

## セットのメモリ使用量の確認方法
  セット型はメモリ効率が悪いことで知られている
  sys.getsizeof(items_in_set)
    """