class RingBuffer:
    def __init__(self, capacity):
        self.oldest = None
        self.storage = []
        self.capacity = capacity

    def append(self, value):
        if self.capacity > 0:
            if self.oldest is None:
                self.storage.append(value)
                self.oldest = 0
            elif len(self.storage) == self.capacity:
                self.storage[self.oldest] = value
                if self.oldest == self.capacity - 1:
                    self.oldest = 0
                else:
                    self.oldest = self.oldest + 1
            else:
                self.storage.append(value)

    def get(self):
        return self.storage
