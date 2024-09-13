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

# 00:00 Korok Forest
# 02:47 Lake Hylia
# 04:56 Stables
# 07:11 Breath Of The Wild
# 09:02 Windfall Island
# 11:11 Knight Academy
# 13:13 Crimson Loftwing
# 15:28 Dragon Roost Island
# 17:28 Tal Tal Heights
# 19:55 Romance In The Air
# 21:23 Kokiri Forest
# 22:36 Rito Village
# 23:39 Skyloft
# 25:18 Outset Island
# 26:33 Windmill Hut
# 27:43 Ordon Village
# 30:34 Hyrule Field
# 33:02 Ordon Ranch
# 34:08 Medli’s Awakening
# 35:10 Mabe Village
# 35:55 Lorule Field
# 37:13 The Legendary Hero
# 39:31 Faron Woods
# 41:35 Tarrey Town
# 43:12 Ocarina Of Time
# 45:19 Title Theme - Twilight
# 46:29 Lurelin Village
# 49:26 Fi’s Gratitude
# 50:44 Zelda’s Ballad
# 52:07 Epilogue
# 53:51 Tears Of The Kingdom
# 56:14 Korok Forest
# 59:01 Lake Hylia
# 1:01:10 Stables
# 1:03:26 Breath Of The Wild
# 1:05:17 Windfall Island
# 1:07:26 Knight Academy
# 1:09:28 Crimson Loftwing
# 1:11:43 Dragon Roost Island
# 1:13:43 Tal Tal Heights
# 1:16:10 Romance In The Air
# 1:17:38 Kokiri Forest
# 1:18:51 Rito Village
# 1:19:53 Skyloft
# 1:21:33 Outset Island
# 1:22:47 Windmill Hut
# 1:23:57 Ordon Village
# 1:26:49 Hyrule Field
# 1:29:19 Ordon Ranch
# 1:30:22 Medli’s Awakening
# 1:31:25 Mabe Village
# 1:32:10 Lorule Field
# 1:33:28 The Legendary Hero
# 1:35:46 Faron Woods
# 1:37:49 Tarrey Town
# 1:39:27 Ocarina Of Time
# 1:41:34 Title Theme - Twilight
# 1:42:44 Lurelin Village
# 1:45:41 Fi’s Gratitude
# 1:46:49 Zelda’s Ballad
# 1:48:22 Epilogue
