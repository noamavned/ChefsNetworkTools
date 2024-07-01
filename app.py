import balloon
import cutie
from functools import lru_cache
import os
import time
title = "NETWORK TOOLS  <***>"


import ipconfig
import hostname
import ping
import netstat
import systeminfo
import wifiHistory


@lru_cache()
def Title(s):
    ball = balloon.BALOON()
    title_new = ball.create_ascii_balloon(s)
    l_spaces = s.count(" ")
    l = (len(s)-l_spaces)*6+(l_spaces*2)+3
    ret = title_new + '\n' + '='*l + '\n'
    return [ret, l]

def clear():
    os.system("cls || clear")

def wait():
    cutie.secure_input("Press enter key to continue . . .")

def printTitle():
    clear()
    print(Title(title)[0])


lastOn = 0
while True:
    printTitle()

    print('CHOOSE WHAT TO DO')
    print("-"*Title(title)[1])
    actions = [
        "Ping",
        "Ipconfig",
        "Systeminfo",
        "Netstat",
        "Hostname",
        "WIFI HISTORY",
        "EXIT",
    ]
    index = cutie.select(actions, selected_index=lastOn)
    lastOn = index
    action = actions[index]
    printTitle()

    l = Title(title)[1]
    match(action):
        case "EXIT":
            time.sleep(0.4)
            print("OK")
            exit()

        case "Ping":
            x = "8.8.8.8"
            if cutie.prompt_yes_or_no('DO YOU WANT TO USE A CUSTOM URL TO PING? (NO WILL RESULT IN "8.8.8.8")'):
                printTitle()
                x = input("ENTER URL: ")
            printTitle()
            ping.print_ping(x, l)
            print("\n")
            wait()
        
        case "Ipconfig":
            print('CHOOSE WHAT TO DO')
            print("-"*l)
            actions2 = [
                "FULL Ipconfig",
                "SIMPLIFIED Ipconfig",
                "GO BACK",
            ]
            action2 = actions2[cutie.select(actions2, selected_index=0)]
            printTitle()

            match(action2):
                case "FULL Ipconfig":
                    ipconfig.print_full_ipconfig(l)
                
                case "SIMPLIFIED Ipconfig":
                    ipconfig.print_simplified_ipconfig(l)

            if action2 != "GO BACK":
                wait()
        
        case "Systeminfo":
            systeminfo.print_systeminfo(l)
            wait()

        case "Netstat":
            netstat.print_netstat(l)
            wait()

        case "Hostname":
            hostname.print_hostname(l)
            wait()

        case "WIFI HISTORY":
            print('CHOOSE WHAT TO DO')
            print("-"*l)
            actions2 = [
                "See profiles on interface Wi-Fi",
                "Get password of a profile on interface Wi-Fi",
                "Get full info of a profile on interface Wi-Fi",
                "GO BACK",
            ]
            action2 = actions2[cutie.select(actions2, selected_index=0)]
            printTitle()

            match(action2):
                case "See profiles on interface Wi-Fi":
                    wifiHistory.print_profiles(l)
                
                case "Get password of a profile on interface Wi-Fi":
                    printTitle()
                    profile = wifiHistory.select_profile(l)
                    printTitle()
                    wifiHistory.print_pass(profile, l)
                
                case "Get full info of a profile on interface Wi-Fi":
                    printTitle()
                    profile = wifiHistory.select_profile(l)
                    printTitle()
                    wifiHistory.print_info(profile, l)

            if action2 != "GO BACK":
                wait()