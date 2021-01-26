#!/usr/bin/python
# -*- coding: utf-8 -*-
"""d_
    display the data's shape, details and data head.


Todo:


"""
import pandas as pd
import matplotlib.pyplot as plt

def d(data):
    columns = data.columns
    df1=data.describe(include='all')

    count=df1.loc['count']
    max=data.shape[0]
    missing=pd.DataFrame(max-count)
    missing=missing.rename(columns={'count':'missing'})
    
    missing_per=missing.apply(lambda x: x / max )
    missing_per=missing_per.rename(columns={'missing':'missing_per'}).T
    
    d_type=pd.DataFrame(data.dtypes)
    d_type=d_type.rename(columns={0:'d_type'})
    
    
    df2=pd.merge(missing, d_type,left_index=True,right_index=True).T
    df2=df2.append(missing_per,sort=False)

    df=df1.append(df2,sort = True)
    df=df=df.reindex(index=['count', 'missing','missing_per','unique','top', 'freq', 'mean', 'std', 'min', '25%', '50%', '75%', 'max','d_type'],columns = columns )
    pd.options.display.float_format = '{:.2f}'.format
    return df

def nan(data):
    """missing data ratio
    """
    
    tmp = data.isna().sum()

    fig = plt.figure(figsize=(16,4))#,dpi=200)
    ax = fig.add_subplot(111)
    ax.bar(tmp.index, tmp.values / len(data) *100, label='Missing Data Ratio')
    ax.bar(tmp.index, (len(data)-tmp.values) / len(data) * 100, bottom=tmp.values/len(data)*100, color='gray', alpha=0.2)
    
#     plt.hlines([50], -1, len(data.columns), "grey", linestyles='dashed')     # hlines
    
    ax.set_title('Missing Data Ratio')
    ax.set_ylabel('Ratio(%)')
    ax.set_xlabel('Columns')
    ax.legend(loc='lower right', bbox_to_anchor=(1,1))
#     ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    ax.set_xticklabels(tmp.index, rotation=90)
    ax.grid(linestyle='--', alpha=0.4)