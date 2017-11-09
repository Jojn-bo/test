import time

print(time.time())#时间戳
print(time.clock())#第一次调用，返回的是进程运行的实际时间
time.sleep(1)
print(time.clock())#第二次调用，显示的是第一次调用到第二次调用中间运行的时间

x = time.localtime()
print(time.gmtime())#返回的是UTC时间元组，中国是UTC+8时区
print(time.localtime())#返回的是UTC+8时间元组，也就是当前地区的时间
print(time.asctime(x))#返回的是时间元组对应的字符串时间
print(time.ctime(3422341221))#返回的是时间戳对应的字符串时间
print(time.mktime(x))#返回指定元组时间与1970.0.0之间的时间戳
