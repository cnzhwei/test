'''
输出当前系统的时间
调用datetime库
'''

from datetime import datetime 
now = datetime.now()
print(now)
now.strftime("%x")
now.strftime("%X")