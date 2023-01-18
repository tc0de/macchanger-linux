from colorama import Fore, Back, Style
import pyhtools
from pyhtools.attackers.Network.machngr import change_mac
from pyhtools.attackers.Network.machngr import generate_random_mac

ascii = (
    '''  

TTTTTTT         CCCCC   OOOOO  DDDDD   EEEEEEE 
  TTT          CC    C OO   OO DD  DD  EE      
  TTT   _____  CC      OO   OO DD   DD EEEEE   
  TTT          CC    C OO   OO DD   DD EE      
  TTT           CCCCC   OOOO0  DDDDDD  EEEEEEE 
                                               
    '''

)

print(Fore.CYAN + ascii)

print(Fore.LIGHTRED_EX + "[*] WORKS ONLY ON LINUX!")


interface = input(Fore.LIGHTBLUE_EX + '[*] Provide an interface (CASE SENSITIVE):  ')
gen = generate_random_mac()
change_mac(intrfc=interface, new_mac=gen)