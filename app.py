# FRAMEWORKS
# FRAMEWORKS
# FRAMEWORKS
from dotenv import load_dotenv
from pynput.keyboard import Controller, Key 
from pynput.mouse import Controller as MouseController, Button
from datetime import datetime
from database_handling import read_csv, write_csv, register_user
from image_analysis import get_screenshot, images_are_similar
from account_information_generator import generate_account_data

import threading
import pyautogui
import time
import asyncio
import random
import os
import psutil
import subprocess

pyautogui.FAILSAFE = False

username_location = [360, 380]
password_location = [360, 430]
login_button_location = [360, 500]

ign_form_location = [325, 310]
ign_confirm_button_location = [535, 315]
ign_okay_button_location = [360, 400]

character_swat_location = [185, 290]
character_omoh_location = [400, 300]
character_sas_location = [620, 300]
character_list = [
    character_swat_location, 
    character_omoh_location, 
    character_sas_location
]
character_to_buy = random.choice(character_list)
character_buy_button_location = [405, 520]
character_okay_button_location = [400, 365]

welcomeback_okay_button_location = [395, 365]

lucky_logo_location = [283, 54]
lucky_spin_button_location = [355, 500]

vpn_below = [170, 580]
vpn_button = [515, 366]

# Controller
# Controller
# Controller
keyboard = Controller()
mouse = MouseController()

def gotothis(data, press = False):
    x = data[0]
    y = data[1]

    # Move mouse smoothly to target
    pyautogui.moveTo(x, y)

    # Sleep for 1 second
    time.sleep(1)

    if press:
        mouse.click(Button.left, 1)
        time.sleep(1)

def press_key(key):
    keyboard.press(key)
    keyboard.release(key) 

def press_word(word):
    for i in word:
        press_key(i)
        time.sleep(0.5)

# 
# 
# 

# OPEN CLIENT
def open_client():
    game_path = r"C:\Program Files (x86)\Crossfire PH\patcher_cf2.exe"
    working_directory = r"C:\Program Files (x86)\Crossfire PH"
    subprocess.Popen(game_path, cwd=working_directory, shell=True)

    time.sleep(100)

# CLOSE CLIENT
def close_client():
    subprocess.run(["taskkill", "/F", "/IM", "crossfire.exe"], shell=True)

# LOGIN PAGE
def login(data):
    gotothis(username_location, True)
    press_word(data['USERNAME'])
    gotothis(password_location, True)
    press_word(data['PASSWORD'])
    gotothis(login_button_location, True)

# IGN SET UP
def ign(data):
    gotothis(ign_form_location, True)
    press_word(data['IGN'])
    gotothis(ign_confirm_button_location, True)
    gotothis(ign_confirm_button_location, True)
    gotothis(ign_okay_button_location, True)

# BUYING CHARACTER
def character():
    gotothis(character_to_buy, True)
    gotothis(character_buy_button_location, True)
    gotothis(character_okay_button_location, True)
    gotothis(welcomeback_okay_button_location, True)

# LUCKY SPIN
def lucky_spin():
    gotothis(welcomeback_okay_button_location, True)
    gotothis(lucky_logo_location, True)
    time.sleep(2)
    for i in range(3):
        gotothis(lucky_spin_button_location, True)
        time.sleep(5)

# START START START
# START START START
# START START START

num = 0
while True:
    account_information = generate_account_data()
    result = asyncio.run(register_user(account_information))

    data = None
    if result:
        data = {
            "USERNAME": account_information["user_id"],
            'PASSWORD': account_information["user_password"],
            "IGN": account_information["ign"]
        }
    
    open_client()
    login(data)
    time.sleep(10)

    ign(data)
    time.sleep(3)
    character()
    time.sleep(3)
    
    lucky_spin()
    close_client()
    num += 1

    if num == 10:
        gotothis(vpn_below, True)
        gotothis(vpn_button, True)
        num = 0

    time.sleep(5)