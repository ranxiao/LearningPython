date, name, price = ['December 23, 2015','Bread Glove', 8.51]
print(date)

def drop_first_last(grades):
    first, *middle, last=grades # all middle ones contained by *
    avg = sum(middle)/len(middle)
    print(avg)
drop_first_last([65,76,98,54,21])