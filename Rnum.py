import string

varCharSet = string.digits + string.ascii_letters + '_'

def gen(x):
    s = '_'
    for i in range(0,x):
        s += '_'
    return [s, x + 1]

def trans(s, x):
    r = ""
    inStr = False
    inChar = False
    maxInt = (1 << 65) - 1
    num = maxInt
    mp = {}
    lst = ''
    for i in s:
        if i.isdigit():
            if inStr or inChar:
                r += i
            else:
                if num == maxInt:
                    num = 0
                num = num * 10 + string.atoi(i)
                num &= maxInt
        else:
            if num < maxInt:
                if num in mp:
                    ts = mp[num]
                else:
                    [ts, x] = gen(x)
                    mp[num] = ts
                r += ts
                num = maxInt
            if i == '"' and lst != '\\' and inChar == False:
                if inStr == True:
                    inStr = False
                else:
                    inStr = True
            if i == "'" and lst != '\\' and inStr == False:
                if inChar == True:
                    inChar = False
                else:
                    inChar = True
            r += i
        lst = i
    r = '\n' + r
    for i in mp:
        ts = 'const long long ' + mp[i] + ' = ' + str(i) + 'LL;\n';
        r = ts + r
    return [r, x + 1]
