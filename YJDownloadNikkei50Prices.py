from pandas.core.frame import DataFrame
from pandas.io import html
import requests
import lxml.html as lh
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from datetime import date
import time

def YJDownloadStockData(symbol, startdate:datetime):



    url = 'https://finance.yahoo.co.jp/quote/' + symbol + '.T/history?from='+startdate.strftime('%Y%m%d')+'&to='+ datetime.now().strftime('%Y%m%d') +  '&timeFrame=d&page=' #+ '1'
    
 #   n_days =  (datetime.today() - startdate).days

    n_days =  np.busday_count( startdate.date(), datetime.today().date() )- 200

    #'https://finance.yahoo.co.jp/quote/8411.T/history?from=20210101&to=20210913&timeFrame=d&page=1'
    #url = '/home/carlo/Downloads/8411.html'

    columns = ['date', 'adjclose']

    wholepage_stock_data = pd.DataFrame()
    

    
    for p in range(1,50):        
        #with open(url+str(i),'r') as f:
            #doc = lh.fromstring(f.read())
        time.sleep(1)
        try:
            page = requests.get(url+str(p))
        except:
            pass
        doc = lh.fromstring(page.content)
        stock_data = pd.DataFrame()
        tr_elements = doc.xpath('//tr')

        col = []
        i = 0

        for t in tr_elements[0]:
            i+=1
            name = t.text_content()
            print (name)



        for j in range(1, len(tr_elements)):
            T = tr_elements[j]
            index = 0
            stockticker = []
            error = False
            for t in T.iterchildren():    
                print(index)
                data = t.text_content()
#                print(data)
                if (index == 0):
                    if(data==''):
                        error = True
                        pass
                    datastring = str(data)
                    datastring = datastring.replace("年", "/")
                    datastring = datastring.replace("月", "/")
                    datastring = datastring.replace("日", "")
                    stockticker.append(datastring)
                
                if (index == 6):
                    stockticker.append(data)
                index+=1
            
            stock_data = stock_data.append(dict(zip(columns, stockticker)), ignore_index=True)
            stock_data = stock_data.dropna()
            print(stock_data.head())
        wholepage_stock_data = wholepage_stock_data.append(stock_data)

    wholepage_stock_data = wholepage_stock_data.dropna()
    wholepage_stock_data.set_index('date')
 #   print(wholepage_stock_data)
    return wholepage_stock_data


def ReadStocksFromFile():
    stocks = pd.DataFrame()
    return stocks


def FormatStocksCSVs():
    i = 0
    stock_prices = pd.DataFrame()
    stock_symbols = pd.DataFrame()
    stock_symbols = pd.read_csv('https://raw.githubusercontent.com/cartasuzuki/phynance/master/datasets/nikkei_high_dividend_yield_50_weight_en.csv', usecols=['Code'])
    for symbol in stock_symbols['Code']:
        myprices = pd.DataFrame()
        myprices = pd.read_csv(str(symbol)+".csv")
        myprices.set_index('date')
        if(i==0):
            stock_prices[['date']] = myprices[['date']]
            stock_prices.set_index('date')
            i = 1
        stock_prices[[str(symbol)]] = myprices[['adjclose']]

    stock_prices.to_csv('nikkei50.csv')


def DownloadAllStocksCSVs():
    fromdate = datetime(2017,1,1)
    stockdata = pd.DataFrame()
    stock_symbols = pd.read_csv('https://raw.githubusercontent.com/cartasuzuki/phynance/master/datasets/nikkei_high_dividend_yield_50_weight_en.csv', usecols=['Code'])
    for symbol in stock_symbols['Code']:
        stockdata = YJDownloadStockData(str(symbol), fromdate)
        stockdata.to_csv(str(symbol)+'.csv')
        print( str(symbol) +'.csv saved')















