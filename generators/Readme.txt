Part 2: Processing Data Files
    nongenlog.py -- Calculate the number of bytes transferred in an Apache server log using a simple for-loop, Does not use generators
    genlog.py    -- Calculate the number of bytes transferred in an Apache server log using a series of generator expression
    makebig.py   -- Make a large access-log file for performance tesing. This will create a file "big-access-log". For the numbers used in the presentation. I used python3 makebig.py 2000.

Part 3: Fun with Files and Directories
    genfind.py   -- A generator function that yields filenames matching a given filename pattern.
    genopen.py   -- A generator function that yields filenames matching a given filename pattern
    gencat.py    -- A generator function that concatenates a sequence of generators into a single sequence
    gengrep.py   -- A generator that greps a series of lines for those that match a regex pattern

Part 4: Parsing and Processing Data
    bytesgen.py  -- Example that finds out how many bytes were transferred for a specific file in a whole directory of log files
    retuple.py   -- Parse a sequence of lines into a sequence of tuples using regular expressions.
    redict.py    -- Parse a sequence of lines into a sequence of dictionaries with named fields.
    fieldmap.py  -- Remap fields in a sequence of dictionaries
    linesdir.py  -- Generate lines from files in a directory
    apachelog.py -- Parse an Apache log file.
    query404.py  -- Find the set of all documents that are broken (404)
    largefiles.py-- Find all requests that transferred over a megabyte.
    largest.py   -- Find the largest document.
    hosts.py     -- Find unique host IP addresses.
    downloads.py -- Find number of downloads of a specific file.
    robots.py    -- Find out who has been hitting robots.txt

Part 5: Processing Infinite Data
    "Tailing a log file results in an "infinite" stream, It costantly watches the file and yields lines as soon as new data is written.
    follow.py    -- Follow a log-file in real-time like tail -f in Unix this program, you need to have a log-file to work with. Run the program runservers.py to start a simulated web-server. This will write a series of log lines for you to follow
    realtime404.py -- Print all 404 requests as thet happen in real-time on a log file.

Part 6: Feeding the Pipeline
    genreceive.py -- Generate clients that connect to a TCP socket.
    genmessages.py-- Generate UDP message
    genevents.py -- Generate a sequence of events on a set of sockets
    genqueue.py  -- Consume items on a queue

Part 7: Extending the Pipeline
    genpickle.py -- Turn sequences of objects into a sequence of pickle
    sendto.py    -- Send a sequence of items to a remote machine via a socket. User genpickle above
    receivefrom.py-- Receive a sequence of items from a socket. Uses genpickle above
    broadcast.py -- Broadcast a sequence of items to a collection of consumers.
    netsend.py   -- Send items to another host on the network. Requires a receive(use receivefrom.py above)
    genmulti.py  -- Generate items from more than one generator at once (multiplexing)

Part 8: Various Programming Tricks (And Debugging)
    gentrace.py -- Example of debugging a generator component
    storelast.py -- Store the last value of a generator (for access later in the processing pipeline)
    genshutdown.py -- Simple example of shutting down a generator.
    shutdownevt.py -- Shutting down a generator with an event

Part 9: Co-routines
    """In Python 2.5, generators picked up the ability to receive values using .send()


    recvcount.py -- A co-routine example
    consumer.py -- Co-routine example with a consumer decorator
    logcoroutine.py -- Processing log files with co-routines
