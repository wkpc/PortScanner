# This is a sample Python script.
import errno
import socket


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def TCPScan(targetIP, sP, fP=65535):
    open = set()
    closed = set()
    filtered = set()

    # start up the scanner on the selected port
    # for IPv4. To use IPv6, use "socket.AF_INET6"
    # for TCP connections. For UDP, use "socket.SOCK_DGRAM"

    # Go through all 65535 ports...
    for i in range(sP, fP, 1):
        # ...and try to connect
        try:
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.settimeout(0.2)

            result = soc.connect_ex((targetIP, i))

            # if a connection was established...
            if result == 0:
                print("open")
                open.add(i)
            # if the port was closed...
            elif result == 1:
                print("closed")
                closed.add(i)
            # if the port did not respond...
            else:
                print("filtered")
                filtered.add(i)

        finally:
            soc.close()

            print("finished scanning")

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
    # collect the host's IP
    hostIp = socket.gethostbyname(socket.gethostname())
    print(hostIp)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
