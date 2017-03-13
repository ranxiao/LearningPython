# build a dictionary
stocks ={
    'GOOG': 520.54,
    'FB':76.45,
    'YHOO':39.28,
    'AMZN':306.21,
    'APPL':99.76
}
# zip the keys and values into a zipped list, then min, max etc can be performed on list, since they can't be performed on dictionary
print(min(zip(stocks.values(),stocks.keys())))
print(max(zip(stocks.values(),stocks.keys())))
# sort operate based on the first input
print(sorted(zip(stocks.values(),stocks.keys())))
