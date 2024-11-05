from CircularQueue import CircularQueue

Queue = CircularQueue(10)

while True :
    command = input("[메뉴선택] i-입력, d-삭제=> ")

    if command == 'i' :
        str = input("  입력할 값: ")
        Queue.enqueue(str)
        print(Queue)

    elif command == 'd' :
        Queue.dequeue()
        print(Queue)