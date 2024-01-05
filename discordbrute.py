import requests
import os
import time
from colorama import Fore,Style
import string
import threading
import random
url = f"https://discord.com/api/v9/invites/vHcvkG7eyJ?with_counts=true&with_expiration=true"

def Menu():
    def GetOptions():
        while True:
            time.sleep(0.5)
            os.system("cls")
            try:
                return int(input("""
                    {3}      DISCORD BRUTE
                    {0} [1] - {1} Temporary Invite (8 lenght)
                    {0} [2] - {1} Permantent Invite (10 lenght)

                    {3}    made by .sneezedip
                    {2}
                ->""".format(Fore.RED,Fore.CYAN,Style.RESET_ALL,Fore.LIGHTRED_EX)))
            except ValueError:
                print(Fore.RED,"Invalid Integer.",Style.RESET_ALL)
    def ValidInput():
        while True:
            time.sleep(0.5)
            os.system("cls")
            try:
                return int(input("How many threads? "))
            except ValueError:
                print(Fore.RED,"Invalid Integer.",Style.RESET_ALL)    
    while True:
        time.sleep(0.5)
        os.system("cls")
        choice = GetOptions()
        threads = ValidInput()
        if choice == 1 or choice == 2:
            if choice == 1:
                StartThread(8,threads)
            else:
                StartThread(10,threads)
        else:
            print(Fore.RED,"Invalid Integer.",Style.RESET_ALL)
def StartThread(len,threads_amount):
    threads = []
    print(Fore.MAGENTA,"STARTING THREADS...")
    for i in range(0, threads_amount):
        thread = threading.Thread(target = GetInv,args=(len,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

def GetInv(l):
    lenght = l
    while True:
        ran_inv = ''.join(random.choices(string.digits+string.ascii_uppercase+string.ascii_lowercase,k=lenght))
        response = requests.get(f"https://discord.com/api/v9/invites/{ran_inv}?with_counts=true&with_expiration=true")
        if response.status_code == 200:
            print(Fore.GREEN,"VALID CODE. ",ran_inv)
            with open("validinvites.txt","a")as file:
                file.write(f"https://discord.com/invite/{ran_inv}")
        else:
            print(Fore.RED,"INVALID CODE. ",ran_inv)    

if __name__ == "__main__":
    Menu()