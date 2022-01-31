#Author : Nemuel Wainaina
#Usage : python scanner.py -t <TARGET> -p <PORT_TO_SCAN>/<START_PORT - END_PORT>

from port_scanner import is_port_open
from colorama import init, Fore

#some color, haha
init()
GREEN = Fore.GREEN
BLUE = Fore.BLUE
RED = Fore.RED
GRAY = Fore.LIGHTBLACK_EX
RESET = Fore.RESET

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description = "Port Scanner")
    parser.add_argument("-t", "--target", dest = "target", required = True)
    parser.add_argument("-p", dest = "ports", required = True)
    
    args = parser.parse_args()
    
    target = args.target
    ports = args.ports
    
    #declare some variables that we will use to keep track of some analytics during the scan
    ports_num = 0
    open_ports = 0
    closed_ports = 0
    
    print(f"\n{BLUE}[*] Scanning {target}{RESET}\n")
    
    if '-' in ports:
        #this means that we are targeting a range of ports
        ports = ports.split('-')
        ports_num = len([p for p in range(int(ports[0]), int(ports[1]) + 1)])
        for p in range(int(ports[0]), int(ports[1]) + 1):
            if is_port_open(target, p):
                open_ports += 1
            else:
                closed_ports += 1
    else:
        #this implies that we are targeting just one port
        ports_num = 1
        if is_port_open(target, ports):
            open_ports += 1
        else:
            closed_ports += 1

    #finalize by printing some analytical information regarding the performed scan
    print(f"{BLUE}\n[*] Scan Completed{RESET}")
    print(f"{BLUE}    {ports_num} Ports Scanned{RESET}")
    print(f"{GREEN}    {open_ports} Ports Open{RESET}")
    print(f"{RED}    {closed_ports} Ports Closed{RESET} ")
    
        
    
    
    
    