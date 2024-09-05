from threading import Semaphore
# It allows multiple threads to wait on the same barrier object instance (e.g. at the same point in code) until 
# a predefined fixed number of threads arrive (e.g. the barrier is full), after which all threads are then notified
#  and released to continue their execution.

# Internally, a barrier maintains a count of the number of threads waiting on the barrier and a configured maximum
#  number of parties (threads) that are expected. Once the expected number of parties reaches the pre-defined maximum, 
# all waiting threads are notified.


class H2O:
    def __init__(self):
        self.barrier = threading.Barrier(3)
        self.h = Semaphore(2)
        self.o = Semaphore(1)
        pass


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.h.acquire()
        self.barrier.wait()
        releaseHydrogen()
        self.h.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.o.acquire()
        self.barrier.wait()
        releaseOxygen()
        self.o.release()