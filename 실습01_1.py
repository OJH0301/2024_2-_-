def contains(bag, e) :
    return e in bag

def insert(bag, e) :
    bag.append(e)

def remove(bag, e) :
    bag.remove(e)

def count(bag):
    return len(bag)

def numOf(bag, e):
    count = 0
    for i in range(len(bag)):
        if bag[i] == e :
            count = count + 1
    return count

myBag = [ ]
insert(myBag, '전화기')
insert(myBag, '교과서')
insert(myBag, '교과서')
insert(myBag, '연필')
insert(myBag, '지우개')
insert(myBag, '연습장')
print('내 가방속의 물건:', myBag)
print('교과서의 개수:', numOf(myBag,'교과서'))
print('연습장의 개수:', numOf(myBag,'연습장'))

insert(myBag, '사전')
remove(myBag, '교과서')
remove(myBag, '연습장')
print('내 가방속의 물건:', myBag)
print('교과서의 개수:', numOf(myBag,'교과서'))
print('연습장의 개수:', numOf(myBag,'연습장'))