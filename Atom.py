from threading import Lock

class Atom:

    def __init__(self, value):
        self.value = value
        self.lock = Lock()

    def read(self):
        with self.lock:
            return self.value

    def update(self, updateFunction):
        with self.lock:
            self.value = updateFunction(self.value)
