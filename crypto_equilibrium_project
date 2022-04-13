import os
import requests
import json
import time
from datetime import datetime, timedelta
from itertools import permutations
from itertools import combinations



import matplotlib.pyplot as plt
import networkx as nx
from networkx.classes.function import path_weight

url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Ceos%2Ccardano%2Cbitcoin-cash%2Cethereum%2Clitecoin&vs_currencies=btc%2Ceos%2Cada%2Cbch%2Ceth%2Cltc'
request = requests.get(url)

#print(request.text)

coins=json.loads(request.text) #Dict name is coins

#coins.update()
g = nx.DiGraph() # Creating a graph

edges = []

for coin in coins:
    #print(line)
    
    if coin == 'bitcoin': #To Change coins into tickers
        coin_ticker = 'btc'
    if coin == 'eos':
        coin_ticker = 'eos'
    if coin == 'cardano':
        coin_ticker = 'ada'
    if coin == 'bitcoin-cash':
        coin_ticker ='bch'
    if coin == 'ethereum':
        coin_ticker = 'eth'
        
    if coin == 'litecoin':
        #print('did it enter')
        coin_ticker = 'ltc'
        #print(coin_ticker)
    
    for node in coins[coin]: #Set the coins and nodes
        weight = coins[coin][node]
        edges.append((coin_ticker,node,weight))
        print(f'edges {edges}\n')
g.add_weighted_edges_from(edges)

input("Press Enter to Continue")
print(g.nodes)


greatest_weight = -99999999
greatest_path = []
lowest_weight = 99999999
lowest_path = []
for n1, n2 in combinations(g.nodes,2):
    print("paths from ", n1, "to", n2, "----------------------------------")
    for path in nx.all_simple_paths(g, source=n1, target=n2):
        print(path)
        # Update this code to multiply all the edges in the path and print
        # the factor
        path_weight_to = 1
        for i in range(len(path)-1):
            #print("edge from",path[i],"to",path[i+1],": ",g[path[i]][path[i+1]]["weight"])
            path_weight_to *= g[path[i]][path[i+1]]["weight"]
        
        path.reverse()
        
        path_weight_from = 1
        for i in range(len(path)-1):
            #print("edge from",path[i],"to",path[i+1],": ",g[path[i]][path[i+1]]["weight"])
            path_weight_from *= g[path[i]][path[i+1]]["weight"]
        
        path_weight_factor = path_weight_to * path_weight_from
        print("path weight factor for path",path,": ",path_weight_factor)
    if path_weight_factor > greatest_weight:
        greatest_weight = path_weight_factor
        greatest_path = path
    
            
print("greatest path",greatest_path, "at weight: ", greatest_weight)
print(0)
