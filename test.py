import sys
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
f = open('test.txt', 'r')
lines = f.readlines()
for line in lines:
    if i == 0:
        currencies, data = get_currencies(line)
    if i == 1:
        s = line
    if i == 2:
        g = line
    i+= 1
print(currencies)
print(data)

rates = [[0.0] * len(currencies) for _ in range(len(currencies))]

for i in range(len(data)):
    data[i] = data[i].split(',')
    data[i][2] = float(data[i][2])

for source, target, value in data:
    source_index = currencies.index(source)
    target_index = currencies.index(target)
    rates[source_index][target_index] = value
    rates[target_index][source_index] = 1 / value

for i in range(len(currencies)):
    rates[i][i] = 1.0
    
    
for i in rates:
    print(i)
