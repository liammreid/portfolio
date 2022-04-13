import json
import requests 
import numpy as np
import time
import pandas as pd
import alpaca_trade_api as tradeapi

def append_data(): #Append the Data
    tickers = ['AAPL','AMZN','TSLA','AMC','FB','MSFT','ZM','COST','GME','NKE'] #Tickers
    for ticker in tickers:
        url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=2N9T7N1L0BO5PFH6' #Url to append data
        print(url)
        request = requests.get(url)
        time.sleep(12)
        rqst_dict = json.loads(request.text)
        
        key_series = 'Time Series (Daily)' #key values
        key_open = '1. open'
        key_close = '4. close'
        key_hi = '2. high'
        key_lo = '3. low'
        
        #file = open(ticker + ".csv")
        #lines = file.readlines()
        #last_line = lines[-1]
        #items = last_line.split(",")
        #last_date = items[0]
        
        last_date = open('/home/ec2-user/environment/final_project/data/'+ticker+".csv").readlines()[-1].split(",")[0] #Update the data
        
        prices = []
        
        for date in rqst_dict[key_series]:
            row = ""
            row += date + ","
            row += rqst_dict[key_series][date][key_open] + ","
            row += rqst_dict[key_series][date][key_hi]+ ","
            row += rqst_dict[key_series][date][key_lo]+ ","
            row += rqst_dict[key_series][date][key_close] + "\n"
            if date > last_date:
                prices.append(row)
        
        prices.reverse()
        
        print(prices)
        
        csv_file = open('/home/ec2-user/environment/final_project/data/'+ticker + ".csv", "a") #Append to CSV File
        #csv_file.write("date,open,hi,lo,close\n")
        
        for row in prices:
            csv_file.write(row)


def simpleMovingAvereage(prices,ticker):
    i = 0
    buy = 0
    tot_profit = 0
    sell=0
    bought=0
    for price in prices:
        if i >= 5:
            avg = ( prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices [i-5])/5 #5 Day Average Code
           # print("avg: ", avg)
            if price < avg and buy == 0: #buy at code
                print("buying at: ", price)
                buy = price
                tot_profit = sell - buy
                sell = 0
                bought +=1
                if i == len(prices)-1:
                    print("buying today")
                    api_key = 'PKON1IH7EUTIKSS02ZP3' #Submit buy to Alpaca
                    api_secret = 'UAWRrfhj5zWx8dU62vqI7Fz1FCNceQC75oQ1gOro'
                    base_url = 'https://paper-api.alpaca.markets'
                    api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
                       
                    api.submit_order(symbol=ticker, 
                    qty=1, 
                    side='buy', 
                    time_in_force='gtc', 
                    type='market')
                if bought ==1:
                    first_buy=price
            elif price > avg and buy != 0:
                print("Selling at: ", price) #Sell at Code#
                tot_profit += price - buy 
                print("Trade profit: ", price - buy)
                buy = 0
                if i == len(prices)-1:
                    print("selling today")
                    api_key = 'PKON1IH7EUTIKSS02ZP3' #Submit buy to Alpaca
                    api_secret = 'UAWRrfhj5zWx8dU62vqI7Fz1FCNceQC75oQ1gOro'
                    base_url = 'https://paper-api.alpaca.markets'
                    api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
                       
                    api.submit_order(symbol=ticker, 
                    qty=1, 
                    side='sell', 
                    time_in_force='gtc', 
                    type='market')
            else: 
                pass
        i+=1
    print ("tot_profit: ", tot_profit)
    final_profit_percentage= (tot_profit/first_buy)*100 #Percentage Return Equation
    return tot_profit, final_profit_percentage

def meanReversionStrategy(prices,ticker):
    i = 0
    buy = 0
    sell = 0
    tot_profit = 0
    bought = 0
    for price in prices:
        if i >= 5:
            avg = ( prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices [i-5])/5 #5 Day Average Code
           # print("avg: ", avg)
            if price < avg *0.95 and buy == 0: #buy at code
                print("buying at: ", price)
                buy = price
                tot_profit = sell - buy
                sell = 0
                bought +=1
                if i == len(prices)-1:
                    print("buying today")
                    api_key = 'PKON1IH7EUTIKSS02ZP3' #Submit buy to Alpaca
                    api_secret = 'UAWRrfhj5zWx8dU62vqI7Fz1FCNceQC75oQ1gOro'
                    base_url = 'https://paper-api.alpaca.markets'
                    api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
                       
                    api.submit_order(symbol=ticker, 
                    qty=1, 
                    side='buy', 
                    time_in_force='gtc', 
                    type='market')
                if bought == 1:
                    first_buy = price
            elif price > avg *1.05 and sell == 0:
                print("Selling at: ", price) #Sell at Code#
                sell=price
                tot_profit += price - buy 
                print("Trade profit: ", price - buy)
                buy = 0
                if i == len(prices)-1:
                    print("selling today")
                    api_key = 'PKON1IH7EUTIKSS02ZP3' #Submit buy to Alpaca
                    api_secret = 'UAWRrfhj5zWx8dU62vqI7Fz1FCNceQC75oQ1gOro'
                    base_url = 'https://paper-api.alpaca.markets'
                    api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
                       
                    api.submit_order(symbol=ticker, 
                    qty=1, 
                    side='sell', 
                    time_in_force='gtc', 
                    type='market')
            else: 
                pass
        i+=1
    print ("tot_profit: ", tot_profit)
    final_profit_percentage= (tot_profit/first_buy)*100 #Percentage Return Equation
    return tot_profit, final_profit_percentage
    
def bollingerBandsStrategy(prices,ticker):
    i = 0
    buy = 0
    sell = 0
    tot_profit = 0
    bought = 0
    for price in prices:
        if i >= 5:
            avg = ( prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices [i-5])/5 #5 Day Average Code
           # print("avg: ", avg)
            if price > avg *1.05: #buy at code
                print("buying at: ", price)
                buy = price
                tot_profit = sell - buy
                sell = 0
                bought +=1
                if i == len(prices)-1:
                    print("buying today")
                    api_key = 'PKON1IH7EUTIKSS02ZP3' #Submit buy to Alpaca
                    api_secret = 'UAWRrfhj5zWx8dU62vqI7Fz1FCNceQC75oQ1gOro'
                    base_url = 'https://paper-api.alpaca.markets'
                    api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
                       
                    api.submit_order(symbol=ticker, 
                    qty=1, 
                    side='buy', 
                    time_in_force='gtc', 
                    type='market')
                if bought == 1:
                    first_buy = price
            elif price < avg *0.95:
                print("Selling at: ", price) #Sell at Code#
                sell=price
                tot_profit += price - buy 
                print("Trade profit: ", price - buy)
                buy = 0
                if i == len(prices)-1:
                    print("selling today")
                    api_key = 'PKON1IH7EUTIKSS02ZP3' #Submit buy to Alpaca
                    api_secret = 'UAWRrfhj5zWx8dU62vqI7Fz1FCNceQC75oQ1gOro'
                    base_url = 'https://paper-api.alpaca.markets'
                    api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
                       
                    api.submit_order(symbol=ticker, 
                    qty=1, 
                    side='sell', 
                    time_in_force='gtc', 
                    type='market')
            else: 
                pass
        i+=1
    print ("tot_profit: ", tot_profit)
    final_profit_percentage= (tot_profit/first_buy)*100 #Percentage Return Equation
    return tot_profit, final_profit_percentage


def saveResults():
    tickers = ['AAPL','AMZN','TSLA','AMC','FB','MSFT','ZM','COST','GME','NKE']
    
    results = {}
    high_returns=0
    high_returns_ticker=0
    high_returns_strategy=0
    
    for ticker in tickers:
        prices = pd.read_csv('final_project/data/'+ticker+'.csv')
        prices = list(prices['close'])
        profit,returns=  simpleMovingAvereage(prices,ticker)
        if returns > high_returns:
            high_returns=returns
            high_returns_ticker=ticker
            high_returns_strategy= 'sma'
        results[ticker+"_sma_profit"]=profit #Stores the profit for the SMA
        results[ticker+"_sma_returns"]=returns #Stores the returns for the SMA
        profit,returns= meanReversionStrategy(prices,ticker)
        if returns > high_returns:
            high_returns=returns
            high_returns_ticker=ticker
            high_returns_strategy= 'mrs'
        results[ticker+"_mrs_profit"]=profit #Stores the profit for the Mean Revision Strategy
        results[ticker+"_mrs_returns"]=returns #Stores the reurns for the Mean Revision Strategy
        profit,returns= bollingerBandsStrategy(prices,ticker)
        if returns > high_returns:
            high_returns=returns
            high_returns_ticker=ticker
            high_returns_strategy= 'bbs' 
        results[ticker+"_bbs_profit"]=profit
        results[ticker+"_bbs_returns"]=returns
    results["high_returns"]=high_returns
    results["high_returns_strategy"]=high_returns_strategy
    results["high_returns_ticker"]=high_returns_ticker
    return results

append_data()
results=saveResults()
json.dump(results, open("/home/ec2-user/environment/final_project/results.json","a"))
