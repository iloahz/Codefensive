import Rvar

f = open('origin.cpp','r')
s = f.read()

s = Rvar.trans(s,0)

print s[0]
