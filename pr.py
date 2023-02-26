def l(num,b):
    num=num.zfill(8)
    l=len(num)
    s=num[b:l]
    s=s+'0'*b
    return s

# print(l('1001',2))

def R(num,b):
    num=num.zfill(8)
    l=len(num)
    s=num[0:l-b]
    s='0'*b+s
    return s

print(R('1001',2))
