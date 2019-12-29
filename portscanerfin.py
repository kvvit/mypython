#!/usr/bin/env python3
import socket
import sys
from datetime import datetime

def scan_ports(remoteServer, firstPort, lastPort):
    remoteServerIP = socket.gethostbyname(remoteServer)

    # Print a nice banner with information on which host we are about to scan
    print("-" * 60)
    print("Please wait, scanning remote host:", remoteServerIP, "Ports from:", firstPort, "to", lastPort)
    print("-" * 60)

    # Check what time the scan started
    t1 = datetime.now()

    try:
        for port in range(firstPort, lastPort):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((remoteServerIP, port))
            #print("Now we scan Port:", port)
            if result == 0:
                print("Port {}:    Open".format(port))
            sock.close()

    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total = t2 - t1

    # Printing the information to screen
    print('Scanning Completed in: ', total)

def main():
    remoteServer = input("Enter a remote host to scan: ")
    firstPort = input("Enter first port in range: ")
    lastPort = input("Enter last port in range: ")
    firstPort = int(firstPort)
    lastPort = int(lastPort)
    scan_ports(remoteServer, firstPort, lastPort)

if __name__ == "__main__":
    main()