#�����β���ʵ��

#�����ĸ���

#print len()#�޲Σ�����ʧ�ܣ�len��Ҫ����

a = "adsfd"
print len(a)

#ʲô���β�

def function1(a,b):
    if a > b:
        print a
    else:
        print b
    

#ʲô��ʵ��

def function2(a,b):
    if a > b:
        print a
    else:
        print b

function2(2,3)


#ȫ�ֱ���
def fun():
    global i
    i = 7
    print i

#i = 9
fun()
#i = 9
print i
