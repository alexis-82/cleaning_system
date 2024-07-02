#!/usr/bin/env python3
import time
import os
import subprocess

def print_with_delay(message, delay=1):
    print(message)
    time.sleep(delay)

def run_command(command, use_sudo=True):
    if use_sudo:
        full_command = f"sudo sh -c '{command}'"
    else:
        full_command = f"su -c '{command}'"
    return subprocess.run(full_command, shell=True, text=True, capture_output=True)

def clean_system(use_sudo):
    commands = [
        ("apt-get update", "Aggiornamento del sistema"),
        ("apt-get upgrade -y", "Upgrade del sistema"),
        ("apt-get install deborphan -y", "Installazione di Deborphan"),
        ("deborphan | xargs apt-get -y remove --purge", "Rimozione librerie non utilizzate"),
        ("apt-get clean", "Pulizia (clean)"),
        ("apt-get autoclean", "Pulizia (autoclean)"),
        ("apt-get autoremove -y", "Rimozione pacchetti non necessari"),
        ("echo 3 > /proc/sys/vm/drop_caches && swapoff -a && swapon -a", "Riduzione uso RAM"),
        ("rm -rf /home/*/.cache/*", "Pulizia Cache"),
        ("rm -f /var/log/*.log /var/log/*.log.* /var/log/syslog* && truncate -s 0 /var/log/wtmp && truncate -s 0 /var/log/btmp", "Pulizia file di log")
    ]

    for command, description in commands:
        print_with_delay(f"\n{description}...")
        result = run_command(command, use_sudo)
        if result.returncode != 0:
            print(f"Errore durante l'esecuzione di '{description}':")
            print(result.stderr)

def main():
    print_with_delay("Riconoscimento sistema root in corso...\n", 2)
    
    use_sudo = os.system("sudo -n true 2>/dev/null") == 0

    if use_sudo:
        print_with_delay("Sistema riconosciuto Sudoers", 2)
    else:
        print_with_delay("Sistema riconosciuto Su", 2)

    clean_system(use_sudo)

    print_with_delay("\nOperazioni di pulizia e aggiornamento completate.", 2)

if __name__ == "__main__":
    main()