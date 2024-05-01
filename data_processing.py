import pandas as pd


def data_processing(file0,file1,file2):
    data0 = pd.read_csv('./data/daily_sales_data_0.csv')
    data1 = pd.read_csv('./data/daily_sales_data_1.csv')
    data2 = pd.read_csv('./data/daily_sales_data_2.csv')
    
    data =  [data0 , data1 , data2]
    data = pd.concat(data)
    
    data = data[data['product']=='pink morsel']
    data['price'] = data['price'].replace('[\$,]', '', regex=True).astype(float)

    data['sales'] = data['price'] * data['quantity']
    
    del data['price']
    del data['quantity']
    
    data = data.reset_index(drop=True)
    data.to_csv('output_file.csv', index=False)



file0 = './data/daily_sales_data_0.csv'
file1 = './data/daily_sales_data_1.csv'
file2 = './data/daily_sales_data_2.csv'

data_processing(file0,file1,file2)