# import hashlib
#
# m = hashlib.md5()
# m.update(b'hello')
# print(m.hexdigest())
# m.update(b'it is me')
# print(m.hexdigest())
# m.update(b'it is been a long time since we spoken...')
# print(m.hexdigest())
#
#
# s2=hashlib.sha1()
# s2.update(b'hello')
# print(s2.hexdigest())
#
# s3=hashlib.sha512()
# s3.update(b'hello')
# print(s3.hexdigest())

import hmac

h = hmac.new('天王盖地虎'.encode(encoding='utf-8'),'你是二百五'.encode(encoding='utf-8'))
print(h.digest())
print(h.hexdigest())