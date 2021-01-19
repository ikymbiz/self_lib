#!/usr/bin/python
# -*- coding: utf-8 -*-
"""d_
    display the data's shape, details and data head.


Todo:


"""
import pandas as pd

def d(data):
    columns = data.columns
    df1=data.describe(include='all')

    count=df1.loc['count']
    max=data.shape[0]
    missing=pd.DataFrame(max-count)
    missing=missing.rename(columns={'count':'missing'})

    d_type=pd.DataFrame(data.dtypes)
    d_type=d_type.rename(columns={0:'d_type'})

    df2=pd.merge(missing, d_type, right_index=True, left_index=True).T

    df=df1.append(df2,sort = True)
    df=df=df.reindex(index=['count', 'missing', 'unique','top', 'freq', 'mean', 'std', 'min', '25%', '50%', '75%', 'max','d_type'],columns = columns )
    pd.options.display.float_format = '{:.2f}'.format
    return df