import requests
import os
import time
from colorama import Fore,Style
import string
import threading
import random
list_of_threads = []
reason = 0
removed_threads = 0
proxies_list = []
proxies_len = 0
current_Index = 0
def Menu():
    global threads,proxies_list,proxies_len
    threads = 0
    time.sleep(0.5)
    def GetOptions():
        while True:
            time.sleep(0.5)
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
            try:
                return int(input("How many threads? "))
            except ValueError:
                print(Fore.RED,"Invalid Integer.",Style.RESET_ALL)    
    def GetProxies():
        with open("proxies.txt","r")as file:
            for line in file:
                proxies_list.append(str(line.replace("\n","")))
    while True:
        time.sleep(0.5)
        os.system("cls")
        choice = GetOptions()
        threads = ValidInput()
        GetProxies()
        proxies_len = len(proxies_list) 
        if choice == 1 or choice == 2:
            if choice == 1:
                StartThread(8,threads)
            else:
                StartThread(10,threads)
        else:
            print(Fore.RED,"Invalid Integer.",Style.RESET_ALL)
def StartThread(len,threads_amount):
    global list_of_threads
    """
        Starts all the threads based on the amount defined by the user
    """
    threads = []
    print(Fore.MAGENTA,"TOTAL PROXIES LOADED : ",proxies_len)
    print(Fore.MAGENTA,"STARTING THREADS...")
    for _ in range(0, threads_amount):
        thread = threading.Thread(target = GetInv,args=(len,))
        thread.start()
        list_of_threads.append(thread.name)
        threads.append(thread)
    for thread in threads:
        thread.join()
def RemoveThreadsAmount():
    global list_of_threads,removed_threads
    if list_of_threads:
        list_of_threads.pop()
        removed_threads += 1
        print(f"{Fore.BLUE}Removed {removed_threads} threads | {len(list_of_threads)} Remaining")    
def write_proxies(proxies):
    with open("proxies.txt", "w") as file:
        for proxy in proxies:
            file.write(f"{proxy}\n") 
def GetInv(l):
    global removed_threads,current_Index,proxies_len
    error_count = 0
    while True:
        if current_Index >= proxies_len:
            break
        try:
            ran_inv = ''.join(random.choices(string.digits+string.ascii_uppercase+string.ascii_lowercase,k=l))
            response = requests.get(f"https://discord.com/api/v9/invites/{ran_inv}?with_counts=true&with_expiration=true",proxies={"http": proxies_list[current_Index], "https": proxies_list[current_Index]}, timeout=8)
            if response.status_code == 200:
                print(Fore.GREEN,"VALID CODE. ",ran_inv)
                with open("validinvites.txt","a")as file:
                    file.write(f"https://discord.com/invite/{ran_inv}")
            elif response.status_code == 429:
                if error_count >= 2:
                    current_Index += 1
                    error_count = 0
                elif error_count >= 5:
                    RemoveThreadsAmount()
                    if not list_of_threads:
                        print(Fore.RED, "Maximum requests reached, and all threads were terminated.")
                        removed_threads = 0
                        time.sleep(1)
                    print(Fore.BLUE,"MAXIMUM REQUESTS!")
                else:
                    print(Fore.RED,"TOO MANY REQUESTS.")  
                    error_count += 1
            else:
                print(Fore.RED,"INVALID CODE. ",ran_inv)  
        except requests.RequestException as e:
            if str(e).__contains__("Max retries"):
                proxies_len -= 1
                print(f"{Fore.MAGENTA} Proxie {proxies_list[current_Index]} not worked and has been removed. | {proxies_len} remaining...") 
                proxies_list.pop(current_Index)
                try:
                    write_proxies(proxies_list)
                except:
                    pass
                current_Index += 1
if __name__ == "__main__":
    Menu()
