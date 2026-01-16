from myasync import event_loop

def test1():
    print("Starting coroutine test1()")

def test2():
    print("Starting coroutine test2()")

def main():
    print("Starting coroutine main()")


loop = event_loop()
loop.run(main())
