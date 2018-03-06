# An Introduction to Python Concurrency 

## Part I -- Some Basic Concepts 
```text
Concurrent Programming

Multitasking
    If only one CPU is available, the only way it can run multiple tasks is by rapidly switching between them 

Parallel Processing 
    If the total number of tasks exceeds the number of CPUs, then each CPU also multitasks 

Task Execution
    All tasks execute by alternating between CPU processing and I/O handling 
    For I/O, tasks must wait(sleep)
    For CPU Bound Tasks,

Shared Memory
    
Processes
    Processes coordinate using IPC 

Distributed Computing 
    Communication via sockets 
```

## Part 2 -- Why Concurrency and Python
```text
Python is interpreted
    "WHat the hardware giveth, the software taketh away"
Python is a very high level language
    Useful data types (dictionaries, lists,etc)
    Network protocols
    Text parsing (regrexs, XML, HTML,etc)
    Files and the file system
    Databases 
Python can be extended with C code 
    It's called "using the right tool for the job"
```

# Part 3 -- Python Thread Programming 
```text
Threads
    Once you start a thread, it runs independently
    Use t.join() to wait for a thread to exit 

Daemonic Threads
Threads share all of the data in your program 
Thread scheduling is non-deterministic 
Operatioins often take several steps and might be interrupted mid-stream (non-atomic)
Access to any kind of shared data is also non-deterministic 
Semaphores
    


countdown.py        -- A very simple thread (a first example)
countdown2.py       -- Launching a function in a thread 
rece.py             -- Example of a race condition. Run multiple times to see different results 
```

# Part 4 -- Thread Synchronization Primitives 
```text
Synchronization Options
    Lock
    RLock
    Semaphore 
    BoundedSemaphore
    Event
    Condition 

Mutex Locks 
    If another thread tries to acquire the lock when its already in use, it gets blocked until the lock is released

Locking Perils
    Managing locks is a lot harder than it lock 

Locks and Deadlock
    Don't write code that acquire more than one mutex lock at a time 
    
RLock Reentrant Mutex Lock 
    Similar to a normal lock except that it can be reacquired multiple times by the same thread 

lock_ex.py          -- An example of using a lock to synchronize access to shared data 
lock_with.py        -- An example of using a lock with 
rlock_ex.py         -- An example of code-based lcoking using a reentrant lock
sema_signal.py      -- An exmaple of using a semaphore for signaling between threads 
event_barrier.py    -- Using an event to implement a synchronization barrier.
event_notify.py     -- Using an event and semaphore to implement a kind of notification mechanism. 
cond.py             -- An examples of setting up a producer-consumer problem with a condition variable 
```

# Part 5 -- Threads and Queues
```text
Queue Library Module
    from queue import Queue 
    
    q = Queue([maxsize])    # Create a queue 
    q.put(item)             # Put an item on the queue 
    q.get()                 # Get an item from the queue 
    q.empty()               # Check if empty
    q.full()                # Check if full 
    q.task_done()           # Signal that work is done 
    q.join()                # Wait for all work to be done 
    
pc_queue.py                 # A producer-consumer problem using threads and queues 
```

# Part 6 -- The Problem with Threads 
```text
perf.py                     # A program that illustrates some performance problems with threads 
```

# Part 7 -- The Inside Story on Python Threads 
```text
Python threads are real system threads 
    POSIX threads (pthreads)
    Windows threads 
Fully managed by the host operating system 
    All scheduling/thread switching 

The Infamous GIL 
    Only one Python thread can execute in the interpreter at once 
    GIL -- global interpreter lock  "controls thread execution"
    The GIL ensures that sure each thread gets exclusive access to the entire interpreter internals when it's running 

GIL Behavior
    Whenever a thread runs, it holds the GIL;However,the GIL is released on blocking I/O 

CPU Bound Processing
    To deal with CPU-bound threads, the interpreter periodically performs a "check"
    By default, every 100 interpreter "ticks"
    
dis -- Disassembler for Python bytecode 

Thread Scheduling
    Python does not have a thread scheduler 
    There is no notion of thread priorities,preemption,round-robin scheduling.
    All threading scheduling is left to the host operating system
    
    All interpreter locking is based on signling
        To acquire the GIL, check if it's free. If not, go to sleep and wait for a signal
        To release the GIL, free it and signal

Multicore GIL Contention
```

# Part 8 -- Final Words on Threads 
```text
I/O Bound Processing
    you're really only limited by the host operating systems's baility to manager and schedule a lot of threads 
```

# Part 9 -- Processes and Messages 
```text
An alternative to threads is to run multiple independent copies of the Python interpreter 

Message Passing
    pickle -- Python object serialization 
    pickle.dumps(someobj) # Return the pickle representation of the object as a bytes object 
    pickle.loads() # 

Message Transport 
    Pipes
    Sockets
    FIFOs
    
Libraries provide access to other systems 
    MPI
    XML-RPC ()


channel.py -- An example of setting up a message channel between processes using the subprocess module 
```

# Part 10 -- the Multiprocessing Module 
```text
Distributed Memory
    With multiprocessing, there are no shared data structures 
Other Features
    Process Pools 进程池
    Shared Object and arrays 

countdownp.py -- A very example of launching a process 
perfmp.py     -- A simple performance test of CPU-bound processes. Compare to the thread example earlier 
pipemp.py     -- An example of a multiprocessing producer/consumer with a piipe 
queuemp.py    -- Using multiprocessing queues 
poolmp.py     -- An example of using a multiprocessing pool 
```

# Part 11 -- Alternatives to Threads and Processes 
```text
Event-driven programming
    Turn all I/O handling into events 
    Do everything through event handlers 
    asyncore,Twisted,etc

Events and Asyncore 

generator.py -- A very simple example of using generators to implement a form of coorperative multitasking 
```