def d_describe(data):
    df1=data.describe(include='all')

    count=df1.loc['count']
    max=data.shape[0]
    missing=pd.DataFrame(max-count)
    missing=missing.rename(columns={'count':'missing'})

    d_type=pd.DataFrame(data.dtypes)
    d_type=d_type.rename(columns={0:'d_type'})

    df2=pd.merge(missing, d_type, right_index=True, left_index=True).T

    df=df1.append(df2,sort = True)
    
    return df.reindex(index=['count', 'missing', 'mean', 'std', 'min', '25%', '50%', '75%', 'max','d_type'])


def d_(data):
    """d_
    display the data's shape, information, details and data head.
    """
    shape=str(data.shape)
    print('> shape')
    print(str(data.shape))
    print('\n')
    print('> info') 
    display(data.info())
    print('> describe') 
    display(d_describe(data))
    print('> head')
    display(data.head())
