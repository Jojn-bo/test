class BO_Exception(Exception):
    def __init__(self,msg):
        self.message = msg

    # def __str__(self):
    #     return self.message

try:
    raise BO_Exception('数据库连不上')
except BO_Exception as e:
    print(e)