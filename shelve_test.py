import shelve
import datetime

info = {'name':'BO','age':24}
test=[1,2,3,4,'5']
test1=datetime.datetime.now()

d = shelve.open('T-T')
# d['info']=info
# d['test']=test
# d['test1']=test1

print(d.get('info'))
print(d.get('test'))
print(d.get('test1'))
