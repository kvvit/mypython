#!/usr/bin/env python3
import socket
import sys
import os


from datetime import datetime
from colorama import Fore, Back, Style


def clear() -> object:
    os.system('clear')


def scan_ports(remoteserver, firstport, lastport):
    remoteserverip = socket.gethostbyname(remoteserver)
    # Print a nice banner with information on which host we are about to scan
    print(Fore.RED)
    print("-" * 80)
    print(Fore.GREEN)
    print("Please wait, scanning remote host:", remoteserverip, "Ports from:", firstport, "to", lastport)
    print(Fore.RED)
    print("-" * 80)
    print(Fore.YELLOW)

    # Check what time the scan started
    t1 = datetime.now()

    try:
        for port in range(firstport, lastport):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((remoteserverip, port))
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
    print(Fore.MAGENTA)
    print('Scanning Completed in: ', total)
    print('\033[39m')


def main() -> object:
    clear()
    print(Fore.CYAN)
    remoteserver = str(input("Enter a remote host to scan: "))
    firstport = int(input("Enter first port in range: "))
    lastport = int(input("Enter last port in range: "))
    scan_ports(remoteserver, firstport, lastport)


if __name__ == "__main__":
    main()
