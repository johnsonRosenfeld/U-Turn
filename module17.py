import RoboPiLib as RPL
import setup
import multiprocessing
import time

#FIRST COMMAND
RPL.servoWrite(0, 1000)
RPL.servoWrite(1, 2000)

# Your foo function
def foo(n):
    for i in range(10000 * n):
        time.sleep(1)

if __name__ == '__main__':
    # Start foo as a process
    p = multiprocessing.Process(target=foo, name="Foo", args=(10,))
    p.start()
    # Wait 10 seconds for foo
    time.sleep(3)
    # Terminate foo
    p.terminate()
    # Cleanup
    p.join()

#SECOND COMMAND
RPL.servoWrite(0, 1000)
RPL.servoWrite(1, 1000)

# Your foo function
def foo(n):
    for i in range(10000 * n):
        time.sleep(1)

if __name__ == '__main__':
    # Start foo as a process
    p = multiprocessing.Process(target=foo, name="Foo", args=(10,))
    p.start()
    # Wait 10 seconds for foo
    time.sleep(5)
    # Terminate foo
    p.terminate()
    # Cleanup
    p.join()

#THIRD COMMAND
RPL.servoWrite(0, 1000)
RPL.servoWrite(1, 2000)

    # Your foo function
    def foo(n):
        for i in range(10000 * n):
            time.sleep(1)

    if __name__ == '__main__':
        # Start foo as a process
        p = multiprocessing.Process(target=foo, name="Foo", args=(10,))
        p.start()
        # Wait 10 seconds for foo
        time.sleep(3)
        # Terminate foo
        p.terminate()
        # Cleanup
        p.join()
