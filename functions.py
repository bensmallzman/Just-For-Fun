# functions.py
# This file holds the program's functions


# sys for command line arguments and exiting,
# socket to connect to port,
# datetime to show start and end times,
# re to check the IPV4 entry
import sys  
import socket
from datetime import datetime
import re
    


# Define target. argv[0] is the name of this script, argv[1] is target IP
def targetDef():
    global targetIP
    try:
        # Check for valid IPV4
        entry = re.compile(r'\d+.\d+.\d+.\d+')
        mo = entry.search(sys.argv[1])
        if mo:
            # Define target
            targetIP = socket.gethostbyname(sys.argv[1])
            # In case it remains open
            socket.setdefaulttimeout(.5)
        else:
            print("Please enter a valid IPV4 following the .py file!")
            sys.exit()            
    # Make sure argv[1] is not empty
    except IndexError:
        print("Please enter a valid IPV4 following the .py file!")
        sys.exit()



def banner(target):
    print('\n' + '#' * 50)
    print(f"Scanning {target}")
    print("Start Time: " + str(datetime.now()))
    print('#' * 50 + '\n')



# Check ports
def portCheck(portDict):
    try:
        for port in portDict.keys():
            # Create a socket (IPV4 family, TCP port)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(.5)
            # Connect to socket at targetIP's port and return error indicator
            result = s.connect_ex((targetIP, port))
            # If no error, add to new dictionary
            if result == 0:
                resultDict.setdefault(port, portDict[port])
            # Close connection
            s.close()
    # Closes loop
    except KeyboardInterrupt:
        print("\nExiting.")
        sys.exit()
    # Address related errors
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    # Other errors?
    except socket.error:
        print("Could not connect.")
        sys.exit()

        

# Print list of open ports
def results(output):
    global keyList
    global valList
    print ("Open Ports:\n")
    # Build 2 column table
    keyList = list(output.keys())
    keyList.insert(0, 'PORT')
    valList = list(output.values())
    valList.insert(0, 'SERVICE')
    table = [keyList, valList]
    colWidths = [0] * len(table)
    if len(keyList) > 1:
        for y in range(len(table)):
            for x in table[y]:
                if colWidths[y] < len(str(x)):
                    colWidths[y] = len(str(x))    
        for i in range(len(table[0])):
            for p in range(len(table)):
                print(table[p][i], end='\t')
            print()
    else:
        print("Ports seem closed. Host may be down.")
    print('\n' + '#' * 50)
    print('Scanning Complete!')
    print("End Time: " + str(datetime.now()))
    print('#' * 50 + '\n')
    
    

resultDict = {}


