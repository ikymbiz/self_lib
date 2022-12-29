import os
from datetime import datetime as dt

import yaml
import pandas as pd
import dask.dataframe as ddf
import dask.multiprocessing

# slack
import requests
import json

# garbage collection
import gc

def read_config():
    with open(os.getcwd() + '\\path.yaml','r') as f:
        config = yaml.safe_load(f)
    return config

def path(filename):
    config = read_config()

    if filename == 'base':
        target_path = config['path']['base']
    elif filename == 'data':
        target_path = config['path']['data']
    else:
        path = config['data'][filename]
        target_path = config['path']['base'] + '\\data' + path

    return target_path

def read_data(filename,large_size=False):
    config = read_config()

    try:
        path = config['data'][filename]
        data_path = config['path']['base'] + '\\data\\' + path
    except:
        path = filename
        data_path = path
    ext = os.path.splitext(path)[1][1:]

    if ext == 'pickle':
        loaded_data = pd.read_pickle(data_path)
    elif ext == 'csv':
        if large_size == True:
            loaded_data = ddf.read_csv(data_path,parse_dates=True)
            loaded_data = loaded_data.compute()
        else:
            loaded_data = pd.read_csv(data_path,encoding="utf_8")
    elif ext == 'json':
        loaded_data = pd.read_json(data_path)
    elif ext == 'xl*':
        loaded_data = pd.read_excel(data_path)
    else:
        loaded_data = 'Error'

    return loaded_data

def to_pickle(filename,to_filename,large_size = False):
    config = read_config()

    to_path = config['data'][to_filename]
    to_data_path = config['path']['base'] + '\\data\\' + to_path

    loaded_data = read_data(filename,large_size)
    loade_data = loaded_data.to_pickle(to_data_path)

    return loaded_data

def isExist(path):
    if os.path.isfile(path):
        return True
    elif os.path.isdir(path):
        return True
    else:
        return False

def isExist_mkdir(path):
    try:
        if os.path.isfile(path):
            pass
            # return True
        elif os.path.isdir(path):
            pass
            # return True
        else:
            os.mkdir(path)
            # return True

    except Exception as e:
        print(e)
        return False

def send_slack(msg_text,d_time=True):
    try:
        config = read_config()
        slack_url = config['slack']['url']

        if d_time == True:
            d = dt.now().strftime('%Y-%m-%d %H:%M:%S')
            msg_text = d + "    " + msg_text
        else:
            pass

        content = {'content-type': 'application/json', 'text': msg_text}
        requests.post(slack_url, data=json.dumps(content))
        return True
    except Exception as e:
        print(e)
        return False

def info(df):
    index = ['mean','std','min','25%','50%','75%','max','unique','top','freq']
    col_list = df.columns
    df_dtype = pd.DataFrame()
    df_info = pd.DataFrame(index = index)
    for col in col_list:
        df_dtype.loc['Dtype',col]=df[col].dtype
        df_dtype.loc['Count',col]=df.shape[0]
        if df[col].dtype=='object':
            df_dtype.loc['Unique',col]=df[col].nunique()
        df_dtype.loc['Missing(cnt)',col]=df[col].isna().sum()
        df_dtype.loc['Missing(%)',col]=(df_dtype.loc['Missing(cnt)',col]/df_dtype.loc['Count',col]*100).round(2)
        df_info[col] = df[col].describe(include='all')
    df_info = pd.concat([df_dtype,df_info])
    return df_info.T

class GroupBy:
    '''Groupby

    '''
    def __init__(self):
        pass
    def setting(self,df,groupby_col,target_col):
        df=df[[groupby_col,target_col]].copy()
        df = df.reset_index()
        df_copy = df.copy()
        df_copy = df_copy.groupby(groupby_col).nth(0)
        df_copy = df_copy.rename(columns={target_col:'v'})
        df_copy['v']=0
        df=pd.merge(df,df_copy,on='index', how='outer')
        df['v']=df['v'].fillna(1)
        df['v']=df['v'].astype('int')
        del df_copy
        gc.collect()
        return df
    def diff(self,df,groupby_col,target_col):
        df=self.setting(df,groupby_col,target_col)
        df[target_col +'_diff']=df[target_col].transform('diff')*df['v']
        df = df.drop([groupby_col,target_col,'index','v'],axis=1)
        df[target_col +'_diff']=df[target_col +'_diff'].fillna(0)
        return df
    def pct(self,df,groupby_col,target_col):
        df=self.setting(df,groupby_col,target_col)
        df[target_col +'_pct']=df[target_col].transform('pct_change')*df['v']
        df = df.drop([groupby_col,target_col,'index','v'],axis=1)
        df[target_col +'_pct']=df[target_col +'_pct'].fillna(0)
        return df

