def bulk(self):
    print('%s is yelling...'%self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print('%s is eating....'%self.name,food)

# d = Dog('niuhuayang')
# choice = input('>>:').strip()
# getattr(d,choice)

names = ['alex','jack']
data = {}


try:
    # open('tes.txt')
    # names[3]
    # data['name']
    a = 1
except (KeyError,IndexError) as e:
    print('没有这个Key',e)
# except IndexError as e:
#     print('列表操作错误',e)
except Exception as e:
    print('出未知错了',e)
else:
    print('一切正常')

finally:
    print('不管有没有错，都执行')
