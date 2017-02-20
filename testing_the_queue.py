import array
# testing with PyTest


class Queue:
    def __init__(self, size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))
        #Массивы очень похожи на списки, но с ограничением на тип данных и размер каждого элемента.
        #   Размер и тип элемента в массиве определяется при его создании

    def empty(self):
        return self.size == 0

    def enqueue(self, x):  # add the to the queue
        if self.size == self.max:
            return False  # if we passed this test the queue is not full
            # and we have a room
        assert self.size >= 0 and self.size <= self.max
        self.data[self.tail] = x  # put the data item to the tail
        self.size += 1  # we increas the size of the queueu
        self.tail += 1  # we moved the tail to point to the next element
        if self.tail == self.head:
            assert (self.size == 0) or (self.size == self.max)
            assert self.tail % self.head == 0
        if self.tail == self.max:
            self.tail = 0  # reset the tail to the point at the zero element of the queue

        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.tail > self.head:
            assert (self.tail - self.head) == self.size
        if self.tail < self.head:
            assert (self.head - self.tail) == (self.max - self.size)
        if self.head == self.max:
            self.head = 0
            assert self.head % self.max == 0

        return x
'''
    def checkRep(self):
        #assert self.size >= 0 and self.size <= self.max
        #if self.tail > self.head:
            assert (self.tail - self.head) == self.size
        if self.tail < self.head:
            assert (self.head - self.tail) == (self.max - self.size)
        #if self.tail == self.head:
            assert (self.size == 0) or (self.size == self.max)
        return
'''

def test_checkRep():
    q = Queue(19)

    assert q.size >= 0 and q.size <= q.max
    if q.tail > q.head:
        assert (q.tail - q.head) == q.size
    if q.tail < q.head:
        assert(q.head-q.tail) == (q.max - q.size)
    if q.tail == q.head:
        assert (q.size == 0) or (q.size == q.max)

    return


def test1():
    q = Queue(3)

    res = q.empty()
    if not res:  # if is the queue not empty
        print("test1 NOT OK")
        return
    res = q.enqueue(10)
    if not res:
        print("test2 NOT OK")
        return
    res = q.enqueue(11)
    if not res:
        print("test3 NOT OK")
        return
    x = q.dequeue()
    if x != 10:
        print("test4 NOT OK")
        return
    x = q.dequeue()
    if x != 11:
        print("test5 NOT OK")
        return
    res = q.empty()
    if not res:
        print("test6 NOT OK")
        return

    return print("          test1 OK")


def test2():
    q = Queue(2)
    '''
    res = q.enqueue(10)
    if 10 not in res:
        print("test2 NOT OK")
        return True
    return False
    '''

    res = q.empty()
    if not res:  # if is the queue not empty
        print("test2.0 NOT OK")
        return

    res = q.enqueue(1)
    if not res:
        print("test2.1 NOT OK")
        return

    res = q.enqueue(2)
    if not res:
        print("test2.4 NOT OK")
        return

    if q.size != q.max:
        print("test2.5 NOT OK")
        return

    if q.tail != 0:
        print("test2.6 NOT OK")
        return
    return print("          test2  OK")


def test3():
    q = Queue(1)

    x = q.dequeue()
    if x!= None:
        print("test3.0 NOT OK")
        return

    res = q.enqueue(1)
    if not res:
        print("test3.1 NOT OK")
        return True


    x = q.dequeue()
    if x!=0 and q.head != 0:
        print("test3.2 NOT OK")
        return

    if q.size == 1:
        print("test3.3 NOT OK")
        return
    return print("          test3  OK")




