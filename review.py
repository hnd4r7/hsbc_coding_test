

# Review 1
def add_to_list(value, my_list=[]):
    """
    Problem: You should not use a mutable default argument my_list=[]. Every time the function is called without explicitly passing a list, the same list will be reused and modified.
    
    Solution: Change the default argument to None and create an empty list inside the function if it's None.
        def add_to_list(value, my_list=None):
            if my_list is None:
                my_list = []
            my_list.append(value)
            return my_list
    """
    my_list.append(value)

    return my_list

 

# Review 2
def format_greeting(name, age):
    """
    Problem: You forgot the f prefix.
    
    Solution: return f"Hello, my name is {name} and I am {age} years old."
    
    """
    return "Hello, my name is {name} and I am {age} years old."

 

# Review 3
class Counter:
    """
    Problem: The __init__ method increments the class attribute count instead of the instance attribute.
    
    Solution: Change self.count += 1 to self.count = 1 and remove the class variable count.
    """

    count = 0

 

    def __init__(self):

        self.count += 1

 

    def get_count(self):

        return self.count

 

# Review 4
import threading

 

class SafeCounter:
    """
    Problem: There is a race condition on the count variable of the `SafeCounter` class. It should be protectd from being accessed by multiple thread simutaneously.
    
    Solution: Use a lock to ensure that only one thread can access and modify the count:
    
    class SafeCounter:
        def __init__(self):
            self.count = 0
            self.lock = threading.Lock()
    
        def increment(self):
            with self.lock:
                self.count += 1
    
    """

    def __init__(self):

        self.count = 0

 

    def increment(self):

        self.count += 1

 

def worker(counter):

    for _ in range(1000):

        counter.increment()

 

counter = SafeCounter()

threads = []

for _ in range(10):

    t = threading.Thread(target=worker, args=(counter,))

    t.start()

    threads.append(t)

 

for t in threads:

    t.join()

 

# Review 5
"""
The line counts[item] =+ 1 should be counts[item] += 1.
"""
def count_occurrences(lst):

    counts = {}

    for item in lst:

        if item in counts:

            counts[item] =+ 1

        else:

            counts[item] = 1

    return counts
