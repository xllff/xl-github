#返回单值

def test():
    i = 7
    return i

print test()

#多返回值

def test2(i,j):
    k = i*j
    return [i,j,k]#可返回list，tuple，和dict

x = test2(4,4)
print x
