"""graph
>> https://qiita.com/takubb/items/e18ea4f7c4ecc8be4a5f

# 単変量データの可視化
> 数値データ用ヒストグラム
- .num_vis(data)

> カテゴリデータ用カウントプロット
- .category_vis(data)

> 全てのカテゴリ×カテゴリの組み合わせ
- cat_cat(data,list_label)

> 全てのカテゴリ×数値の組み合わせ
- num_cat(data,list_cat,list_num)

# 相関の可視化
> 数値×数値
- pairplot
>> sns.pairplot(data=raw, vars=['Age', 'Fare'], size=3)

>> sns.pairplot(data=raw, vars=['Age', 'Fare'], hue='Sex', kind='reg', diag_kind='kde', size=3,
            plot_kws={'scatter_kws': {'alpha': 0.4},'line_kws': {'linestyle': '--', 'linewidth': .7}})

    # kind='reg'で回帰直線を追加
    # diag_kind='kde'でヒストグラムをカーネル密度推定で表現
    # hueで層別塗り分け

> 数値×カテゴリ
- ボックスプロット
>> sns.boxplot(data=raw, x='Label', y='Age', palette="Set3")

- .cmp_box(ol_vis=0,**kwargs):
> 箱ひげ図を並べて表示する

> カテゴリ×カテゴリ
- ヒートマップ
>> plt.figure(figsize=(6, 5))
   sns.heatmap(raw[['Age', 'Fare']].corr(), fmt="1.2f", annot=True, lw=0.7, cmap='YlGnBu')

> 割合を示す
- 円グラフ
>> per_pie(Series)

- .duplex(**kwargs)
グラフを重ねて表示する

"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_palette("husl")
sns.set_theme(style="whitegrid")
sns.color_palette("Set1", 24)
sns.set(context='poster',
        style='ticks',
        palette='muted')


def num_vis(data):
    """num_vis(data)
    # 数値データ用ヒストグラム
    """
    data.hist(figsize=(5, 4), color='darkblue', alpha=.7)
    mean = data.mean()
    median = data.median()
    ymax = pd.cut(data, 10).value_counts().max()
    plt.vlines(x=mean, ymin=0, ymax=ymax, colors='red', linestyles='--', lw=.7)# 平均値の直線追加
    plt.annotate('Mean: {}'.format(round(mean, 2)),xy=(mean, ymax), color='red')
    plt.vlines(x=median, ymin=0, ymax=ymax, colors='orange', linestyles='--', lw=.7)# 中央値の直線追加
    plt.annotate('Median: {}'.format(round(median, 2)),xy=(mean, ymax*0.8), color='orange')
    plt.title(data.name)
    plt.show()

def category_vis(data):
    """category_vis(data)
    # カテゴリデータ用カウントプロット
    """
    t = data.value_counts()
    t.plot.bar(figsize=(5, 4), color='indianred', alpha=.7)
    for i in range(len(t)):
        plt.annotate(t[i], xy=(i, t[i]/2), ha='center')#haでannotatioinのテキストを中央寄せ
    plt.title(data.name)
    plt.show()


def graph_type(ax,g_type,value,**kwargs):
    """graphの出力タイプ
    """
    if g_type == "line":
            ax.plot(value,label=kwargs["label"],color=kwargs["color"],linewidth=3,marker="o")
#     elif g_type =="hist":
#         cnt_bins=len(value)
#         ax.hist(value,bins=cnt_bins,label=kwargs["label"],color=kwargs["color"])
#     elif g_type =="box":
#             ax.boxplot(value,label=kwargs["label"],color=kwargs["color"])
    elif g_type =="bar":
        x=kwargs["x"]
        ax.bar(x,value,label=kwargs["label"],color=kwargs["color"])
    else:
        pass

def dataType_ch_np(data):
    """ndarrayにして返す
https://qiita.com/hatorijobs/items/8246e90db6b18d75338c
    """
    if (type(data) is pd.core.frame.DataFrame):
        print("enable: numpy.ndarray or pandas.Series")
        return False,data
    if (type(data) is list):
        data=np.ndarray(data)
        return True,data
    if (type(data) is np.ndarray):
        return True,data
    if (type(data) is pd.core.series.Series):
        data=data.to_numpy()
        return True,data

        
def duplex(**kwargs):
    """グラフを重ねて表示する
    ===================== sample ============================
import pandas as pd
data = pd.DataFrame({"2000Y"  : [12,10,16,19],
                 "2020Y": [14,12,17,23]})

g=graph()
g.duplex(main_title="T month compare",
     x_title="Month",
     x_rotation=45,
     x_scale=[[0,1,2,3],["Jan","Feb","Mar","Apr"]],
     y_title="Temparature",
     y_scale=[[10,15,20,25],["10C","15C","20C","25C"]],
     y_rotation=90,
     g_type=["line","line"],
     g_data=[data['2000Y'],data['2020Y']],
     label=["2000Y","2020Y"],
     color=["Red","steelblue"])

color : https://pythondatascience.plavox.info/wp-content/uploads/2016/06/colorpalette.png

    """
    # グラフの事象設定
    plt.figure(1,figsize=(10,5))

    # グラフの象限の設定
    row,col,pos=1,1,1
    ax=plt.subplot(row, col, pos)

    # グラフの重複数設定
    duple=len(kwargs["g_type"])

    # グラフのデータ設定
    main_title=kwargs.get("main_title")
    x_title=kwargs.get("x_title")
    x_scale=kwargs.get("x_scale")

    if x_scale is None:
        pass
    else:
        x_scale,x_scale_label=x_scale

    x_rotation=kwargs.get("x_rotation",0)
    y_title=kwargs.get("y_title")
    y_scale=kwargs.get("y_scale")

    if y_scale is None:
        pass
    else:
        y_scale,y_scale_label=y_scale

    y_rotation=kwargs.get("y_rotation",90)
    g_type=kwargs["g_type"]
    g_data=kwargs["g_data"]
    label=kwargs.get("label")
    color=kwargs.get("color")
    
    i=0
    for i in range(duple):
        value = g_data[i]
        graph_type(ax,g_type[i],value,label=label[i],x=x_scale,color=color[i])
        i +=1

    # 軸の目盛りラベル
    if x_scale is None:
        pass
    else:
        plt.xticks(x_scale,x_scale_label,rotation=x_rotation)
    if y_scale is None:
        pass
    else:
        plt.yticks(y_scale,y_scale_label)

    # グラフの凡例
    plt.legend()

    # グラフのタイトル /ラベル
    plt.title(main_title)
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    
    plt.show()
        
def cmp_box(ol_vis=0,**kwargs):
    """箱ひげ図を並べて表示する

# 外れ値のマーク
# https://matplotlib.org/3.1.1/api/markers_api.html


===================== sample =========================
cmp_box(ol_vis=0,
    title="コンロ数別の賃料比較",
    x_title="コンロの数",
    y_title= "price",
    labels=["1口","2口","3口","4口以上","不明"],
    dataset=[cor_data2['price'][cor_data2['C1']==1],
    cor_data2['price'][cor_data2['C2']==1],
    cor_data2['price'][cor_data2['C3']==1],
    cor_data2['price'][cor_data2['C4']==1],
    cor_data2['price'][cor_data2['Cn']==1]])
    """
    for s in kwargs["dataset"]:
        result,data=dataType_ch_np(s)
        if result == False:
            break
        else:
            pass

    data = kwargs["dataset"]
    labels = kwargs.get("labels","")
    title = kwargs.get("title","")
    x_title = kwargs.get("x_title","")
    y_title = kwargs.get("y_title","")

    # グラフの事象設定
    ratio=1.5
    height=len(kwargs["dataset"])*ratio
    width=len(kwargs["dataset"])
    plt.figure(1,figsize=(height,width))
    row,col,pos=1,1,1
    ax=plt.subplot(row,col,pos)

    if ol_vis==0:
    # 外れ値を表示する
        ax.boxplot(data,labels=labels,meanline=True,sym="rx")
    elif ol_vis==1:
    # 外れ値を表示しない
        ax.boxplot(data,labels=labels,meanline=True,sym="")
    elif ol_vis==2:
    # 外れ値の計算そのものをやめる(本来の最大値・最小値に基づいてひげを出す)
        ax.boxplot(data,labels=labels,meanline=True,whis="range")

    # グラフのタイトル /ラベル
    plt.title(title)
    plt.xlabel(x_title)
    plt.ylabel(y_title)

def per_pie(Series):
    """ per_pie(Series)
    割合を示す円グラフ
    """
    labels=Series.value_counts().index.to_numpy()
    values=Series.value_counts().to_numpy()
    plt.pie(x=values,
            labels=labels,
            autopct='%.1f%%',
            startangle=90,
            counterclock=True,
            pctdistance=0.6,
            labeldistance=0.15,
            textprops={'color':'white','weight':'bold','size':15},
            frame=False)
    plt.axis('equal')
    plt.show()

def cat_cat(data,list_label):
    """cat_cat(data,list_label)
        全てのカテゴリ×カテゴリの組み合わせ

    """
    plt.figure(figsize=(20, 7))
    plt.subplots_adjust(wspace=0.1, hspace=0.4)
    i = 1
    for label_1 in list_label:
        for label_2 in list_label:
            plt.subplot(3, 3,i)
            sns.heatmap(pd.crosstab(data[label_1], data[label_2]), fmt="1.1f", annot=True, lw=0.7, cmap='Blues')
            i += 1

def num_cat(data,list_cat,list_num):
    """num_cat(data,list_cat,list_num)
    全てのカテゴリ×数値の組み合わせ
    """
    plt.figure(figsize=(20, 7))
    plt.subplots_adjust(wspace=0.1, hspace=0.4)
    i = 1
    for x in list_cat:
        for y in list_num:
            plt.subplot(3, 3, i)
            sns.boxplot(data=data, x=x, y=y, palette="Set3")
            i += 1