from pandas import Series, DataFrame

a = '123.3'
b = '234.23'
c = '31.23'
d = '321.12'

raw_data = {'shape' : [float(a)], 'max_tem' : [float(b)]}
raw_data2 = {'shape' : [float(c)], 'max_tem' : [float(d)]}

dd = DataFrame(raw_data2)
ff = DataFrame(raw_data)

for i in range (1,10):
    ff = ff.append(dd)
    print(i)


print(ff)