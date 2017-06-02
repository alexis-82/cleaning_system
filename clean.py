#!/usr/bin/env python2

import time
import os

print
print "Riconoscimento sistema root in corso...\n"
log = os.system("grep -om1 sudo $HOME/.bash_history > log")
check = open("log", "r")
root = check.read(4 - 0)
if root == "sudo":
    time.sleep(2)
    print "Sistema riconosciuto Sudoers"
    
    time.sleep(1)
    print
    print "Inizio sistema di aggiornamento\n"
    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade -y")

    # Installation library Deborphan
    print
    print "Installatzione di Deborphan\n"
    time.sleep(1)
    os.system("sudo apt-get install deborphan")

    # Apply Deborphan
    time.sleep(1)
    print
    print "Rimozione librerie non utilizzate\n"
    os.system("sudo deborphan | xargs apt-get -y remove --purge")
    
    time.sleep(1)
    print 
    print "Inizio sistema di pulizia\n"
    print "Clean..."
    os.system("sudo apt-get clean")
    print "Autoclean..."
    os.system("sudo apt-get autoclean")
    print "Autoremove..."
    os.system("sudo apt-get autoremove")

    time.sleep(1)
    print
    print "Riduzione uso RAM\n"
    os.system("sudo echo 3 > /proc/sys/vm/drop_caches && swapoff -a && swapon -a")

else:
    time.sleep(2)
    print "Sistema riconosciuto Su"
    
    time.sleep(1)
    print
    print "Inizio sistema di aggiornamento\n"
    os.system("su root -c 'apt-get update'")
    os.system("su root -c 'apt-get upgrade -y'")
    
    # Installation library Deborphan
    print
    print "Installatzione di Deborphan\n"
    time.sleep(1)
    os.system("su root -c 'apt-get install deborphan'")
    
    # Apply Deborphan
    time.sleep(1)
    print
    print "Rimozione librerie non utilizzate\n"
    os.system("su root -c 'deborphan | xargs apt-get -y remove --purge'") 
    
    time.sleep(1)
    print
    print "Inizio sistema di pulizia\n"                                                                                                                                                   
    print "Clean..."
    os.system("su root -c 'apt-get clean'")
    print "Autoclean..."
    os.system("su root -c 'apt-get autoclean'")
    print "Autoremove..."
    os.system("su root -c 'apt-get autoremove'")
    
    time.sleep(1)
    print
    print "Riduzione uso RAM\n"
    os.system("su root -c 'echo 3 > /proc/sys/vm/drop_caches && swapoff -a && swapon -a'")
