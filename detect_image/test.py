def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i * i


mygenerator = createGenerator()  # 제너레이터 생성
print(mygenerator)  # mygenerator object1.
for i in mygenerator:
    print(i)
print(mygenerator)  # mygenerator object1.
for i in mygenerator:
    print(i)
mygenerator = createGenerator()
print(mygenerator)  # mygenerator object2.
for i in mygenerator:
    print(i)
