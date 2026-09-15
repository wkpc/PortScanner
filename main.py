import math
import socket
import sys
import time
from concurrent.futures import ThreadPoolExecutor


"""
Given an IP address and a port number, scans to see if the port is open, closed, or filtered.
:param targetIP The IPv4 address of the target. Can also use the hostname of the target, but may cause problems with the
        DNS lookup.
:param p The port number of the port to be scanned
"""
def TCPScan(targetIP, p):
    # try to connect to the given port #
    try:
        # for IPv4. To use IPv6, use "socket.AF_INET6"
        # for TCP connections. For UDP, use "socket.SOCK_DGRAM"
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.settimeout(0.2)

        result = soc.connect_ex((targetIP, p))

        # if a connection was established...
        if result == 0:
            return "open"
        # if the port was closed...
        elif result == 1:
            return "closed"
        # if the port did not respond...
        else:
            return "filtered"

    finally:
        soc.close()


def SYNScan(targetIP, sP, fP):
    print("")

def UDPcan(targetIP, sP, fP):
    print("")

def ACKScan(targetIP, sP, fP):
    print("")

def FINScan(targetIP, sP, fP):
    print("")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # turn the arguments into input
    # collect the target IP
    targetIp = sys.argv[1]
    print(targetIp)

    # collect the upper and lower bound port numbers
    lP = 1  # default lower bound to 1 (inclusive)
    try:
        lp = int(sys.argv[2])
    except:
        pass
    print(lP)
    hP = 65536  # default upper bound to 65536 (exclusive)
    try:
        hP = int(sys.argv[3])
    except:
        pass
    print(hP)

    # calculate the number of threads needed for the scan
    numOfPorts = hP-lP
    numOfThreads = math.ceil(numOfPorts / 75) # with 0.2s time out/connection, each thread should handle no more than 75 ports for a max scan time of 15s

    # start the timer
    startT = time.time()

    # create the threads and start assigning port numbers to scan
    with ThreadPoolExecutor(max_workers=numOfThreads) as exe:
        results = {i: exe.submit(TCPScan, targetIp, i) for i in range(lP, hP)}

    # let user know how long the scan took
    endT = time.time()
    print("finished scanning. Time elapsed: %.2f" % (endT - startT))

    print("results")
    for port in results:
        rString = results.get(port).result()
        if rString == "open":
            print("Port %i: [%s]"%(port, results.get(port).result()))