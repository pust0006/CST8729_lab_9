def txtToCsv(a,b,c):
    a1 = open(a)
    b1 = open(b)
    c1 = open(c, 'w')
    c1.write('{}\n'.format("First Name, Count"))
    for line in a1:
        name = line.split(' ')
        c1.write("{}".format(name[0] + ", " + name[1]))
    for line in b1:
        name = line.split(' ')
        c1.write("{}".format(name[0] + ", " + name[1]))
    c1.close()
    a1.close()
    b1.close()
a = '2000_BoysNames.txt'
b = '2000_GirlsNames.txt'
c = 'ys.csv'
txtToCsv(a,b,c)
# 2
def csvExp(d):
    try:
        f = open(d,'r')
        for i in f:
            LIST = i.split(',')
            print(LIST)
    except: print('done')
d = input('csv file you wish to read: ')
csvExp(d)
