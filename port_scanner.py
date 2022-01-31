#Author : Nemuel Wainaina

import socket
from colorama import init, Fore

#some color, haha
init()
GREEN = Fore.GREEN
BLUE = Fore.BLUE
RED = Fore.RED
GRAY = Fore.LIGHTBLACK_EX
RESET = Fore.RESET

def is_port_open(target, port):
    '''
    This function simply attempts to create a connection
    to the target machine on the specified port and
    based on whether or not the connection is successful,
    prints to the user whether or not the port is open
    '''
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        print(f"{GREEN}[+] Port {port} is Open {RESET}")
        return True
    except:
        #Comment out the line in order to exclude the results for closed ports
        print(f"{GRAY}[-] Port {port} is Closed {RESET}")
        return False
    finally:
        s.close()
        
        

    
    