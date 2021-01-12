import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

"""graph
- tips

- .duplex(**kwargs)
グラフを重ねて表示する

- .cmp_box(ol_vis=0,**kwargs):
箱ひげ図を並べて表示する

"""



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