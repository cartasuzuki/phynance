#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 15:40:58 2018

@author: carlo
"""

import pandas as pd
import time
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
import numpy as np
import matplotlib.pyplot as plt

class PortfolioOptimizer:
    
    def __init__(self):
        self.key = "1G2GNXJQ2J8MGQ3L"
    
    
    def get_stock_prices(stock_symbols):
        key = "1G2GNXJQ2J8MGQ3L"
        print("Downloading prices from alphavantage.co")
        stocks = pd.DataFrame(columns=stock_symbols)
        count = 0
        for symbol in stock_symbols:
           print(symbol)           
           request_string = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' + symbol + '&apikey=' + key +'&datatype=csv&outputsize=full'
           data = pd.read_csv(request_string ,index_col= ['timestamp'], parse_dates= ['timestamp'])
           adjclose = data['adjusted_close']
           stocks[symbol] = adjclose
           if (count == 4):
               print("sleeping")
               time.sleep(60)
               count = 0
           count = count + 1    
        stocks.dropna(inplace = True)
        return(stocks)
    
    def optimize_portfolio(stocks, min_allocation, max_allocation=1):
        exp_ret = -expected_returns.mean_historical_return(stocks)
        S = risk_models.sample_cov(stocks)
    
        ef = EfficientFrontier(exp_ret, S, gamma = 1, weight_bounds = (min_allocation,max_allocation))
        weights = ef.max_sharpe()
        ret, vol, sharpe = ef.portfolio_performance(verbose=False)
        return(weights, sharpe, ret)
        
    def print_portfolio_result(weights, sharpe, ret):
        for s in weights:
            weights[s] = round(weights[s],2)
            ss = s + ": " + str(weights[s]*100) + "%"
            if(weights[s] > 0.04):
                print(ss)
        print("Sharpe: " + str(round(sharpe,2)) )
        print("Exp. Return: " + str(round(ret*100,2)) )

    def portfolioAsPieChart(weights):
        symbolList = []
        weightList = []
        for s, w in weights.items():
            tempS = s
            tempW = w
            if(tempW > 0.001):
                symbolList.append(tempS)
                weightList.append(tempW)
    
        weightArray = np.array(weightList)
        plt.pie(x = weightArray, labels = symbolList)
        
    def expected_returns_and_cov(stocks):
        exp_ret = -expected_returns.mean_historical_return(stocks)
        S = risk_models.sample_cov(stocks)
        print("Cov: " + str(round(S,2)) )
        print("Exp. Return: " + str(round(exp_ret*100,2)) )
            