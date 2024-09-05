# https://stackoverflow.com/questions/787803/how-does-a-threading-thread-yield-the-rest-of-its-quantum-in-python
# In Python, there isn't a direct equivalent of std::this_thread::yield() as in C++. However, Python provides a similar behavior using the time.sleep(0) function, which gives up the CPU and allows other threads to run. This approach mimics yielding behavior in Python's multithreading context.

# Yielding in Python using time.sleep(0)
# You can use time.sleep(0) to yield the CPU in Python, allowing other threads to run, but keeping the thread in a runnable state, similar to how yielding works in other languages.

#  example using threading to demonstrate yielding:


import threading
import time

# Function where we will use time.sleep(0) to yield
def thread_function(name):
    for i in range(5):
        print(f"Thread {name}: {i}")
        # Yield the CPU to let other threads run
        time.sleep(0)  # This acts like yielding the CPU
    print(f"Thread {name} finished")

# Create multiple threads
thread1 = threading.Thread(target=thread_function, args=("A",))
thread2 = threading.Thread(target=thread_function, args=("B",))

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("All threads completed.")