# 输入温度转换成华氏温度或者摄氏温度，循环转换
# edit by zhwei

Tempstr = input("请输入带符号的温度： ")
while Tempstr[-1] not in ['N','n']:
    if Tempstr[-1] in ['F','f']:
        C = (int(Tempstr[0:-1])-32)/1.8
        print("转换后的温度：{:.2f} C".format(C))
    elif Tempstr[-1] in ['C','c']:
        F = 1.8*int(Tempstr[0:-1])+32
        print("转换后的温度：{:.2f} F".format(F))
    else:
        print("Error!")
    Tempstr = input("请输入带符号的温度： ")