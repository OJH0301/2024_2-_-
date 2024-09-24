from ArrayStack import ArrayStack

map =[[ '1', '1', '1', '1', '1', '1', '1', '1', '1', '1' ],
	  [ 'e', '0', '0', '0', '0', '0', '0', '1', '0', '1' ],
	  [ '1', '1', '0', '1', '0', '1', '0', '1', '0', '1' ],
	  [ '1', '0', '0', '1', '0', '1', '0', '0', '0', '1' ],
	  [ '1', '1', '1', '0', '0', '1', '0', '1', '0', '1' ],
	  [ '1', '1', '0', '0', '1', '1', '1', '0', '0', '1' ],
      [ '1', '0', '0', '1', '0', '0', '0', '1', '1', '1' ],
      [ '1', '0', '1', '0', '0', '1', '0', '0', '1', '1' ],
      [ '1', '0', '0', '0', '1', '1', '1', '0', '0', 'x' ],
      [ '1', '1', '1', '1', '1', '1', '1', '1', '1', '1' ]]
MAZE_SIZE = 10
move = 0

def isValidPos(x, y) :
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE :
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False


def DFS() :
    print('DFS: ')
    stack = ArrayStack(100)
    stack.push((0,1))
    global move

    while not stack.isEmpty():
        here = stack.pop()
        print(here, end='->')
        (x,y) = here

        if (map[y][x] == 'x') :
            return True
        else :
            map[y][x] = '.'
            if isValidPos(x, y - 1):
                stack.push((x, y - 1))
                move += 1
            if isValidPos(x + 1, y):
                stack.push((x + 1, y))
                move += 1
            if isValidPos(x, y + 1):
                stack.push((x, y + 1))
                move += 1
            if isValidPos(x - 1, y):
                stack.push((x - 1, y))
                move += 1
        print(' 현재 스택: ', stack)
    return False

result = DFS()
if result :
    print(' --> 미로탐색 성공')
    print("이동거리", move)
else :
    print(' --> 미로탐색 실패')