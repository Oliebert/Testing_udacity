# testing with PyTest
# CORRECT SPECIFICATION:
#
# the Queue class provides a fixed-size FIFO queue of integers
#
# the constructor takes a single parameter: an integer > 0 that
# is the maximum number of elements the queue can hold.
#
# empty() returns True if and only if the queue currently
# holds no elements, and False otherwise.
#
# full() returns True if and only if the queue cannot hold
# any more elements, and False otherwise.
#
# enqueue(i) attempts to put the integer i into the queue; it returns
# True if successful and False if the queue is full.
#
# dequeue() removes an integer from the queue and returns it,
# or else returns None if the queue is empty.
#
# Example:
# q = Queue(1)
# is_empty = q.empty()
# succeeded = q.enqueue(10)
# is_full = q.full()
# value = q.dequeue()
#
# 1. Should create a Queue q that can only hold 1 element
# 2. Should then check whether q is empty, which should return True
# 3. Should attempt to put 10 into the queue, and return True
# 4. Should check whether q is now full, which should return True
# 5. Should attempt to dequeue and put the result into value, which
#    should be 10
#
# Your test function should run assertion checks and throw an
# AssertionError for each of the 5 incorrect Queues. Pressing
# submit will tell you how many you successfully catch so far.


import array

class Queue:
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if self.size == self.max:
            return False
        x = x % (2**16)# 2 byte integer only untill 65535

        '''
        (2^16 - 1) or 65535 or 0xFFFF or "64k" is the maximum value of 2 bytes. For a long time CPUs used 16-bit architecture and OSes were likewise based on 16-bit operations
        and "words". There were 16-bit commands and 16-bit memory addresses. A lot of systems/compilers still use 16 bits for integers.
        So, (2^16 - 1) is special because it is the largest number that a 16-bit (unsigned) integer can hold and the largest memory address that a 16-bit architecture can access.
        In Python integers will automatically switch from a fixed-size int representation into a variable width long representation
        once you pass the value sys.maxint, which is either 2^31 - 1 or 2^63 - 1 depending on your platform.
         9,223,372,036,854,775,807 is an integer equal to 2^63 − 1
        '''
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 1
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

def test():
    q = Queue(1)
    assert q.size >= 0 and q.size <= q.max
    is_empty = q.empty()
    assert is_empty
    succeeded = q.enqueue(10000) # platform win32 C long nicht mehr als 2147483647
                                     # platform win64 C long nicht mehr als 9,223,372,036,854,775,807
    assert succeeded == True

    is_full = q.full()
    assert is_full

    value = q.dequeue()
    assert value ==10000

