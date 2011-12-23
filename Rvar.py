import string

dataType = ['void', 'bool', 'char', 'int', 'long', 'float', 'double', '__int64', 'string']
varCharSet = string.digits + string.ascii_letters + '_'
blank = [' ','\n','\r','\t']
endSign = ['{', ';']
leftQuote = ['(', '[']
rightQuote = [')', ']']
mp = {}

def gen(x):
    s = '_'
    for i in range(0,x):
        s += '_'
    return [s, x + 1]

def parseInQuote(s,i,x,wh):
    ls = len(s)
    ts = ''
    while i < ls and s[i] != rightQuote[wh]:
        ts += s[i]
        i += 1
    return [ts+s[i],i+1,x]

def getVariable(s,i,x):
    ls = len(s)
    ts = ''
    flag = True
    while flag:
        var = ''
        while i < ls and s[i] in blank:
            ts += s[i]
            i += 1
        while i < ls and s[i] in varCharSet:
            var += s[i]
            i += 1
##        print 'var = ', var
##        print 's[i] = ', s[i]
        if var == '':
            pass
        elif var[0].isdigit():
            ts += var
        elif var == 'main':
            ts += var
        elif var in dataType:
            ts += var
        elif mp.has_key(var):
            ts += mp[var]
        else:
            ts1 = ''
            [ts1, x] = gen(x)
            mp[var] = ts1
            ts += ts1
##            print var, '=', ts1
        if s[i] in leftQuote:
            ts2 = ''
            [ts2,i,x] = parseInQuote(s,i,x,leftQuote.index(s[i]))
            ts += ts2
        elif s[i] == ',':
            ts += s[i]
            i += 1
        elif s[i] in endSign:
            flag = False
            break
        else:
            ts += s[i]
            i += 1
    return [ts, i, x]
        

def parse(s,i,x):
##    print 'parsing from %d _%s_' % (i,s[i])
    ls = len(s)
    ts = ''
    if s[i:i+8] == '#include':
        while i < ls and s[i] != '>':
            ts += s[i]
            i += 1
        return [ts+s[i],i+1,x]
    hold = 0
    flag = True
    while flag:
        flag = False
        for j in dataType:
            l = len(j)
            if i+l < ls and s[i:i+l] == j and s[i+l] not in varCharSet:
                ts += j
                i += l
                flag = True
                break
        if flag:
            hold += 1
            while i < ls and s[i] in blank:
                ts += s[i]
                i += 1
    if hold == 0:
        return [ts+s[i], i + 1, x]
    tts = ''
    [tts, i, x] = getVariable(s,i,x)
    ts += tts
    return [ts+s[i], i + 1, x]

def replace(s):
    ls = len(s)
    i = 1
    ts = s[0]
    inStr = False
    inChar = False
    while i < ls:
        if s[i] == '"':
            ts += s[i]
            i += 1
            while i < ls and (s[i] != '"' or (s[i]=='"' and s[i-1]=='\\')):
                ts += s[i]
                i += 1
            ts += s[i]
            i += 1
        if s[i] == "'":
            ts += s[i]
            i += 1
            while i < ls and (s[i] != "'" or (s[i]=="'" and s[i-1]=='\\')):
                ts += s[i]
                i += 1
            ts += s[i]
            i += 1
        if s[i] in varCharSet and s[i-1] not in varCharSet:
            ts1 = ''
            while i < ls and s[i] in varCharSet:
                ts1 += s[i]
                i += 1
            if mp.has_key(ts1):
                ts += mp[ts1]
            else:
                ts += ts1
        else:
            ts += s[i]
            i += 1
    return ts
            

def trans(s, x):
    r = ''
    ls = len(s)
    i = 0
    while i < ls:
        [ts, i, x] = parse(s,i,x)
        r += ts
##        print r
    r = replace(r)
    return [r, x]
