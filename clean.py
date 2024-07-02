#!/usr/bin/env python3

import time
import os

print()
print("Riconoscimento sistema root in corso...\n")
log = os.system("grep -om1 sudo $HOME/.bash_history > log")
check = open("log", "r")
root = check.read(4 - 0)
if root == "sudo":
    time.sleep(2)
    print("Sistema riconosciuto Sudoers")
    
    time.sleep(1)
    print()
    print("Inizio sistema di aggiornamento\n")
    print()
    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade -y")

    # Installation library Deborphan
    print()
    print("Installatzione di Deborphan\n")
    time.sleep(1)
    print()
    os.system("sudo apt-get install deborphan")

    # Apply Deborphan
    time.sleep(1)
    print()
    print("Rimozione librerie non utilizzate\n")
    print()
    os.system("sudo deborphan | xargs sudo apt-get -y remove --purge")
    
    time.sleep(1)
    print("Inizio sistema di pulizia\n")
    print("Clean...")
    print()
    os.system("sudo apt-get clean")
    print("Autoclean...")
    print()
    os.system("sudo apt-get autoclean")
    print()
    print("Autoremove...")
    os.system("sudo apt-get autoremove")

    time.sleep(1)
    print()
    print("Riduzione uso RAM\n")
    print()
    os.system("sudo sh -c 'echo 3 > /proc/sys/vm/drop_caches && swapoff -a && swapon -a'")
    
    time.sleep(1)
    print()
    print("Pulizia Cache\n")
    print()
    os.system("rm -rf ~/.cache/*")


else:
    time.sleep(2)
    print("Sistema riconosciuto Su")
    
    time.sleep(1)
    print()
    print("Inizio sistema di aggiornamento\n")
    print()
    os.system("su root -c 'apt-get update'")
    os.system("su root -c 'apt-get upgrade -y'")
    
    # Installation library Deborphan
    print()
    print("Installatzione di Deborphan\n")
    print()
    time.sleep(1)
    os.system("su root -c 'apt-get install deborphan'")
    
    # Apply Deborphan
    time.sleep(1)
    print()
    print("Rimozione librerie non utilizzate\n")
    print()
    os.system("su root -c 'deborphan | xargs apt-get -y remove --purge'") 
    
    time.sleep(1)
    print()
    print("Inizio sistema di pulizia\n") 
    print()                                                                                                                                                  
    print("Clean...")
    os.system("su root -c 'apt-get clean'")
    print("Autoclean...")
    os.system("su root -c 'apt-get autoclean'")
    print("Autoremove...")
    os.system("su root -c 'apt-get autoremove'")
    
    time.sleep(1)
    print()
    print("Riduzione uso RAM\n")
    print()
    os.system("su root -c 'echo 3 > /proc/sys/vm/drop_caches && swapoff -a && swapon -a'")
    
    time.sleep(1)
    print()
    print("Pulizia Cache\n")
    print()
    os.system("su root -c 'rm -rf ~/.cache/*'")

