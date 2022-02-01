from threading import Thread, Lock

from Atom import Atom

class RingThread(Thread):

    currentThread = Atom(0)
    shouldFinish = Atom(False)

    def __init__(self, number: int, message: str, currentThreadLock: Lock, messageLock: Lock):
        Thread.__init__(self)
        self.number = number
        self.message = [char for char in message]
        self.currentThreadLock = currentThreadLock
        self.messageLock = messageLock

    def processMessage(self):
        with self.messageLock:
            for i in range(80):
                if not self.message[i].isupper():
                    self.message[i] = self.message[i].upper()
                    RingThread.currentThread.update(lambda x: (x + 1) % 30)
                    return
            
            print(''.join(self.message))
            RingThread.shouldFinish.update(lambda _: True)

    def run(self):
        while not RingThread.shouldFinish.read():
            if self.number == RingThread.currentThread.read():
                self.processMessage()
