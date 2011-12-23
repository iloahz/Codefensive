import Rnum
import Rvar

def trans(s):
    x = 0
    [s, x] = Rvar.trans(s,x)
    [s, x] = Rnum.trans(s,x)
    return s
