import random
import string

from thread import RingThread
from threading import Lock

message = ''.join(random.choice(string.ascii_letters) for _ in range(80))
messageLock = Lock()
currentThreadLock = Lock()

threads = [RingThread(i, message, currentThreadLock, messageLock) for i in range(30)]

print(f'Mensagem a ser circulada: {message}')

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
