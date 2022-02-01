import random
import string
from constants import MAX_THREADS, MESSAGE_LENGTH

from thread import RingThread
from threading import Lock

message = ''.join(random.choice(string.ascii_letters) for _ in range(MESSAGE_LENGTH))
messageLock = Lock()
currentThreadLock = Lock()

threads = [RingThread(i, message, currentThreadLock, messageLock) for i in range(MAX_THREADS)]

print(f'Mensagem a ser circulada: {message}')

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
