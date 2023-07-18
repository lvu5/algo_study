import sys
from math import log
# import numpy as np
# import pandas as pd
# from sklearn import ...
i = 0
currencies = []
data = []
def get_currencies(line):
    temp = line.split(";")
    temp[-1] = temp[-1][:-1]
    data = temp.copy()
    for i in temp:
        currency_list = i.split(',')
        for currency in currency_list[:2]:
            if currency not in currencies:
                currencies.append(currency)
    return currencies, data

s = ""
g = ""

for line in sys.stdin:
    if i == 0:
        currencies, data = get_currencies(line)
    if i == 1:
        s = line[:-1]
    if i == 2:
        g = line[:-1]
    i+= 1

rates = [[0.1] * len(currencies) for _ in range(len(currencies))]

for i in range(len(data)):
    data[i] = data[i].split(',')
    data[i][2] = float(data[i][2])
    


for source, target, value in data:
    source_index = currencies.index(source)
    target_index = currencies.index(target)
    rates[source_index][target_index] = value
    rates[target_index][source_index] = 1.0 / value

for i in range(len(currencies)):
    rates[i][i] = 1.0
    
def negate(graph):
    res = [[-log(edge) for edge in row] for row in graph]
    return res

res = -float('inf')
check = False

#def check_graph(a, b, what):
    

def solve(currencies, rates_matrix):
    global res
    global check
    trans_graph = negate(rates_matrix)
    source = currencies.index(s)
    
    n = len(trans_graph)
    min_dist = [float('inf')] * n
    
    pre = [-1] * n
    min_dist[source] = source
    
    for _ in range(n - 1):
        for source_curr in range(n):
            for dest_curr in range(n):
                if min_dist[dest_curr] > min_dist[source_curr] + trans_graph[source_curr][dest_curr]:
                    min_dist[dest_curr] = min_dist[source_curr] + trans_graph[source_curr][dest_curr]
                    pre[dest_curr] = source_curr
                    
    for source_curr in range(n):
        for dest_curr in range(n):
            if min_dist[dest_curr] > min_dist[source_curr] + trans_graph[source_curr][dest_curr]:
                print_cycle = [dest_curr, source_curr]
                
                while pre[source_curr] not in print_cycle:
                    print_cycle.append(pre[source_curr])
                    source_curr = pre[source_curr]
                print_cycle.append(pre[source_curr])
                # process here
                test = 1.0
                test_cycle = print_cycle[::-1]
                s0 = currencies.index(s)
                g0 = currencies.index(g)
                if s0 in test_cycle and g0 in test_cycle:
                    if test_cycle.index(s0) < test_cycle.index(g0):
                        check = True
                        for node in range(len(test_cycle) - 2):
                            test = test * rates_matrix[test_cycle[node]][test_cycle[node+1]]
                            res = max(res, test)

solve(currencies, rates)

if check == False:
    print(-1.0)
else:
    print(res)
